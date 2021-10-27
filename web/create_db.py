
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, ForeignKey

from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Text

engine = create_engine("sqlite:///db.sqlite")

Base = declarative_base()

Base.metadata.create_all(engine)


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


class Cita(Base):
    __tablename__ = 'citas'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_medico = Column(Integer, ForeignKey(Medico.id), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id), nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    tipo = Column(String)
    motivo = Column(Text)

    medico = relationship('Medico', foreign_keys='Cita.id_medico')
    paciente = relationship('Paciente', foreign_keys='Cita.id_paciente')


class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_medico = Column(Integer, ForeignKey(Medico.id), nullable=False)
    id_paciente = Column(Integer, ForeignKey(Paciente.id), nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    comentarios = Column(Text)

    medico = relationship('Medico', foreign_keys='HistoriaClinica.id_medico')
    paciente = relationship(
        'Paciente', foreign_keys='HistoriaClinica.id_paciente')
