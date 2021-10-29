from flask import Blueprint, json, jsonify, request
from sqlalchemy.orm import Session
from web.create_db import Paciente, engine


doctors_blueprint = Blueprint('doctors', __name__)
