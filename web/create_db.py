
from enum import auto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # for configuration
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column
# create declarative_base instance
from sqlalchemy.sql.sqltypes import Integer, String
from .app import engine
# we'll add classes here#creates a create_engine instance at the bottom of the file
Base = declarative_base()

Base.metadata.create_all(engine)


class Medico(Base):
    __tablename__ = 'medico'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)
    especialidad = Column(String)


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)
    especialidad = Column(String)
