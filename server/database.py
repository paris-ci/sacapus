from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# Définition structure BDD

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    fullname = Column(String(100), nullable=False)
    password = Column(String(64), nullable=False)  # Hashed as SHA256

    def __repr__(self):
        return f"<User(id={self.id},name='{self.name}', fullname='{self.fullname}')>"


class Login(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String(64), nullable=False)
    revoked = Column(Boolean(), default=False, nullable=False)

    user = relationship("User", back_populates="logins")

    def __repr__(self):
        return f"<UserLogin(user_id={self.user_id}, token={self.token})>"


User.logins = relationship("Login", order_by=Login.id, back_populates="user")


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    location = Column(String(64), nullable=False)
    datetime = Column(DateTime(), nullable=False)
    confidence = Column(Float(5))

    user = relationship("User", back_populates="positions")

    def __repr__(self):
        return f"<UserPosition(user_id={self.user_id}, location={self.location}, confidence={self.confidence}, datetime={self.datetime})>"


User.positions = relationship("Position", order_by=Position.id, back_populates="user")


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(64), nullable=False)
    arguments = Column(String(1024), nullable=True)
    completed = Column(Boolean(), nullable=False)
    datetime = Column(DateTime(), nullable=False)

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<UserTask(user_id={self.user_id}, type={self.type}, arguments={self.arguments}, datetime={self.datetime}, completed={self.completed})>"


User.tasks = relationship("Task", order_by=Task.id, back_populates="user")

engine = create_engine('sqlite:///db.sqlite')  # , echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
