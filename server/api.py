import datetime
import os
import time
from uuid import uuid4

import hug
import hashlib
from utils import init_logger
import database

logger = init_logger()
api = hug.API(__name__)


def check_auth(user_name, token):
    session = database.Session()
    login = session.query(database.Login).filter_by(token=token).first()
    if not login:
        return False

    if login.user.name == user_name:
        logger.debug(f"User authed in (with token): {login.user}, with token {login}")
        return login.user
    else:
        logger.warning(f"Failed auth (with token) for {user_name}, with token {token}")
        return False


uuid_token_authentication = hug.authentication.basic(check_auth)

api.http.add_middleware(hug.middleware.LogMiddleware(logger))


def hash_password(password, salt):
    """
    Securely hash a password using a provided salt
    :param password:
    :param salt:
    :return: Hex encoded SHA512 hash of provided password
    """
    password = str(password).encode('utf-8')
    salt = str(salt).encode('utf-8')
    return hashlib.sha512(password + salt).hexdigest()


@hug.post(versions=1)
def login(user_name: hug.types.text, user_password: hug.types.text):
    hash_pass = hash_password(user_password, user_name)

    session = database.Session()
    user = session.query(database.User).filter_by(name=user_name).first()

    if user and user.password == hash_pass:
        new_token = str(uuid4())
        new_login = database.Login(user_id=user.id, token=new_token)
        session.add(new_login)
        session.commit()
        logger.info(f"User logged in : {user}, with token {new_login}")
        return new_token

    else:
        logger.warning(f"Failed login for {user_name} / Requesting {user}")

        return False


@hug.post(versions=1)
def register(user_name: str, user_fullname: str, user_password: str):
    hash_pass = hash_password(user_password, user_name)
    new_user = database.User(name=user_name, fullname=user_fullname, password=hash_pass)
    session = database.Session()
    try:
        session.add(new_user)
        session.commit()
        logger.info(f"User registered : {new_user}")
    except:
        logger.info(f"User not registered because of an error: {new_user}")
        return False

    return True


@hug.post(versions=1, requires=uuid_token_authentication)
def post_position(user: hug.directives.user, location: str, time: int = None, confidence: float = 1):
    if time is None:
        time = datetime.datetime.now()
    else:
        time = datetime.datetime.fromtimestamp(time)

    new_position = database.Position(user_id=user.id, location=location, datetime=time, confidence=confidence)
    session = database.Session()
    session.add(new_position)
    session.commit()
    logger.info(f"New position added for {user} : {new_position}")


@hug.get(versions=1, requires=uuid_token_authentication)
def get_positions(user: hug.directives.user, after=None, before=None):
    positions_list = []

    for position in user.positions:
        positions_list.append({"id": position.id, "location": position.location, "datetime": time.mktime(position.datetime.timetuple()), "confidence": position.confidence})

    return positions_list


@hug.post(versions=1, requires=uuid_token_authentication)
def create_task(user: hug.directives.user, type: str, arguments: str = None):
    new_task = database.Task(user_id=user.id, type=type, arguments=arguments, datetime=datetime.datetime.now(), completed=False)
    session = database.Session()
    session.add(new_task)
    session.commit()
    logger.info(f"New task added for {user} : {new_task}")
    return True


@hug.get(versions=1, requires=uuid_token_authentication)
def get_unfinished_tasks(user: hug.directives.user):
    task_list = []

    for task in user.tasks:
        if not task.completed:
            task_list.append({"id": task.id, "type": task.type, "arguments": task.arguments, "datetime": time.mktime(task.datetime.timetuple()), "completed": False})

    return task_list


@hug.post(versions=1, requires=uuid_token_authentication)
def finish_task(user: hug.directives.user, id: int):
    session = database.Session()
    task = session.query(database.Task).filter_by(id=id).first()
    if task.user.id == user.id:
        task.completed = True
    session.commit()
    logger.info(f"Completed task for {user} : {task}")
    return True


@hug.get(versions=1, requires=uuid_token_authentication)
def user_info(user: hug.directives.user):
    return {"user_name": user.name, "fullname": user.fullname}
