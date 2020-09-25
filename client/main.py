import tqdm

print('start')

import shutil
CUI = True

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : logging'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1

    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import logging

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : os'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import os

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : time'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import time

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours :'.center(x-2) + '*')
    print('*' + 'démarrage du module WiFi'.center(x-2) + '*')

    y_left -= 6

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

time.sleep(5)  # Attente du démarrage

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : collections'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import collections

if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : WhereAmI'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import whereami


if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : utils'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

import utils


if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : API'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

API_URL = "http://sacapus.api-d.com:8000/"
API_VERSION = "v1"
COMPLETE_API_URL = API_URL + API_VERSION + "/"
AUTH = None


if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : Réseau'.center(x-2) + '*')

    y_left -= 5

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)


import requests
from requests.auth import HTTPBasicAuth


if CUI:
    x, y = shutil.get_terminal_size((80, 20))
    y = y - 1

    y_left = y

    print('*' * x)
    print('*' + 'Démarrage de Sacapus en cours!'.center(x-2) + '*')
    print('*' + 'Veuillez patienter'.center(x-2) + '*')
    print('*' + ''.center(x-2) + '*')
    print('*' + 'Initialisation en cours : Finalisation'.center(x-2) + '*')
    print('*' + 'Chargement du modele de données'.center(x-2) + '*')

    y_left -= 6

    y_left -= 1
    for i in range(y_left):print('*' + ' ' * (x-2) + '*')
    print('*' * x)

from whereami import learn
from whereami import get_pipeline
from whereami import predict, predict_proba, crossval, locations

logger = utils.init_logger()
if CUI:
    logger.setLevel(logging.WARNING)



Later = collections.namedtuple('Later', ['path', 'method', 'data'])


class Api():
    def __init__(self, user, password):
        self.user_name = user
        self.token = False
        while not self.token:
            try:
                self.token = self.call_api("login", {"user_name": user, "user_password": password}, offline=False)
            except ConnectionError:
                continue

        self._tasks = collections.deque()
        self._send_later = collections.deque()

    def do_tasks(self):
        for i in range(len(self._send_later)):
            task = self._send_later.popleft()
            try:
                self.call_api(path=task.path, data=task.data, method=task.method, offline=False)
            except ConnectionError:
                self._send_later.appendleft(task)

    def call_api(self, path, data=None, method=requests.post, offline=True):
        """
        Appelle l'api comme définie.

        Exemple :
            call_api("login", {"name":name})

        """
        if data is None:
            data = {}
        url = COMPLETE_API_URL + path

        try:
            if self.token:
                res = method(url, data, auth=HTTPBasicAuth(self.user_name, self.token))
            else:
                res = method(url, data)

        except ConnectionError:
            if offline and method == requests.post:
                self._send_later.append(Later(path=path, data=data, method=method))
                return len(self._send_later)
            elif offline:
                return {}
            else:
                raise

        js = res.json()

        if type(js) == dict and "errors" in js.keys():
            raise Exception(str(js["errors"]))

        return js

    def send_location(self):
        for i in range(1, 4):
            if CUI:
                x, y = shutil.get_terminal_size((80, 20))
                y = y - 1

                y_left = y

                print('*' * x)
                print('*' + 'Recherche en cours de la position'.center(x-2) + '*')
                print('*' + ''.center(x-2) + '*')
                print('*' + 'La position de sacapus est automatiquement déterminée'.center(x-2) + '*')
                print('*' + 'Patientez SVP'.center(x-2) + '*')

                y_left -= 5

                y_left -= 1
                for i in range(y_left):print('*' + ' ' * (x-2) + '*')
                print('*' * x)

            # 3 essais si confidence est trop faible
            try:
                locations = predict_proba()
            except whereami.pipeline.LearnLocation:
                locations = {"Pas de piece aprise": 1}
            location = max(locations, key=locations.get)
            confidence = locations[location]

            if confidence <= 0.40 and i <= 3:
                logger.debug(f"Confidence trop faible ({confidence}), on ré-essaye une mesure (essais restants : {3 - i})")
                time.sleep(15)
                continue

            logger.info(f"Envoi de la postion au serveur avec location={location} et confidence={confidence}")

            if CUI:
                x, y = shutil.get_terminal_size((80, 20))
                y = y - 1

                y_left = y

                print('*' * x)
                print('*' + 'Projet Sacapus'.center(x-2) + '*')
                print('*' + 'Arthur Jovart, 2018'.center(x-2) + '*')
                print('*' + ''.center(x-2) + '*')
                print('*' + 'Projet Libre'.center(x-2) + '*')
                print('*' + 'Institut Villebon Georges Charpak'.center(x-2) + '*')


                print('*' + '-' *(x - 2) + '*')
                print('*' + '\033[1m' + 'Sacapus s\'est géolocalisé'.center(x-2) + '\033[0m' + '*')
                print('*' + ''.center(x-2) + '*')
                print('*' + '\033[1m' + 'La position actuellement détectée est : '.center(x-2) + '\033[0m' + '*')
                print('*' + '\033[0;31m\033[1m' + location.center(x-2) + '\033[0m' + '*')
                print('*' + ''.center(x-2) + '*')
                print('*' + '\033[1m' + 'Pourcentage de confiance : '.center(x-2) + '\033[0m' + '*')
                print('*' + '\033[0;32m\033[1m' + (str(round(confidence * 100))+ '%').center(x-2) + '\033[0m' + '*')

                y_left -= 14

                y_left -= 1
                for i in range(y_left):print('*' + ' ' * (x-2) + '*')
                print('*' * x)

            self.call_api("post_position", {"location": location, "confidence": confidence})
            break

    def get_task(self):
        self.do_tasks()  # Taches réseau

        if len(self._tasks) == 0:
            self._tasks = collections.deque(self.call_api("get_unfinished_tasks", method=requests.get))

        if len(self._tasks):

            task = self._tasks.popleft()
            self.call_api("finish_task", {"id": task["id"]})
            return task

        else:
            return None


def act_task(task):
    if task["type"] == "locate":
        api.send_location()

    elif task["type"] == "learn":
        logger.warning(f"Learning here for {task['arguments'].lower()}")
        logger.debug("")
        try:
            learn(task["arguments"].lower(), n=45)
        except:
            os.system('sudo reboot')


api = Api("Arthur", "lol")
iteration = 0

while True:
    TEMPS = 15
    # 1ere chose, envoyer notre position
    api.send_location()
    end = time.time() + TEMPS

    for i in tqdm.trange(TEMPS):

        logger.debug(f"Iteration {iteration}")
        iteration += 1

        # Regarder si l'on à des choses particulieres à faire
        task = api.get_task()

        while task:

            logger.info(f"Got task : {task}")
            act_task(task)
            task = api.get_task()

        # Enfin, attendre la suite
        time.sleep((end - time.time())/(TEMPS-i))

