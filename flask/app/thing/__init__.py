from flask import Blueprint

bp = Blueprint("thing", __name__)

from app.thing import routes  # noqa: F401, E402
