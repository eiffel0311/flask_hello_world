from flask import Blueprint

api = Blueprint('api', __name__)

from app.api import meta_db, meta_table, meta_source