from itsdangerous import json
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, ForeignKey

from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Text

engine = create_engine("sqlite:///db.sqlite")

Base = declarative_base()


def json_default(ordered_dict):
    return ordered_dict.__dict__


class Medico(Base):
    __tablename__ = 'medicos'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String)
    telefono = Column(String)
    especialidad = Column(String)
    contraseña = Column(String)
    email = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)

    citas = relationship("Cita", back_populates='medico')
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates='medico')


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    fecha_de_nacimiento = Column(DateTime)
    email = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)

    citas = relationship("Cita", back_populates='paciente')
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates='paciente')


class Cita(Base):
    __tablename__ = 'citas'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_medico = Column(Integer, ForeignKey(Medico.id), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id), nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    tipo = Column(String)
    motivo = Column(Text)
    precio = Column(Text)

    medico = relationship('Medico', back_populates="citas")
    paciente = relationship('Paciente', back_populates="citas")

    def __init__(self, id_medico, id_paciente, fecha, tipo, motivo, precio):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.tipo = tipo
        self.motivo = motivo
        self.precio = precio

    def __repr__(self):
        return json.dumps(self, default=json_default, indent=4)

    def __str__(self):
        return self.id


class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_medico = Column(Integer, ForeignKey(Medico.id), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id), nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    comentarios = Column(Text)

    medico = relationship('Medico', back_populates='historias_clinicas')
    paciente = relationship(
        'Paciente', back_populates='historias_clinicas')


Base.metadata.create_all(engine)
