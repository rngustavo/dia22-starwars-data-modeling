import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water =  Column(Integer, nullable=False)
    population =  Column(Integer, nullable=False)
    url = Column(String(250), nullable=False)


class Users(Base):
    __tablename__ = 'users'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
   
    id = Column(Integer, primary_key=True)
    tipo = Column(Integer, nullable=False)
    favorite_id = Column(Integer, nullable=False)
    usuario_id = Column(Integer,ForeignKey('users.id'))
    users = relationship(Users) 
    #inicialmente se hace solo una relacion de favoritos con usuarios
    #dado que se usa tipo de favorito no se usa relacion con las otras
    #dos tablas people y planets

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')