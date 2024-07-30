import json
from datetime import datetime, timezone

from app import db
from app.models import Thing
from app.thing import bp
from jsonschema import ValidationError, validate
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, Conflict, HTTPException, InternalServerError

from flask import Response, request, url_for

# JSON schema for validation
with open("openapi.json") as json_file:
    openapi = json.load(json_file)
thing_schema = openapi["components"]["schemas"]["ThingRequest"]


@bp.route("/things", methods=["POST"])
def create() -> Response:
    """Create a Thing"""
    try:
        validate(instance=request.json, schema=thing_schema)
    except ValidationError as e:
        raise BadRequest(description=e.message)
    else:
        thing = Thing(
            name=request.json["name"],
            colour=request.json["colour"],
            quantity=request.json["quantity"],
        )
        db.session.add(thing)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise Conflict()
    except Exception:
        db.session.rollback()
        raise InternalServerError()
    else:
        response = Response(
            response=repr(thing),
            mimetype="application/json",
            status=201,
        )

        response.headers["Location"] = url_for("thing.get", id=thing.id)
        return response
    finally:
        db.session.close()


@bp.route("/things", methods=["GET"])
def list() -> Response:
    """Get a list of Things"""
    things = [thing.as_dict() for thing in db.session.execute(db.select(Thing).order_by(Thing.created_at)).scalars()]

    return Response(
        response=json.dumps(things, separators=(",", ":")),
        mimetype="application/json",
        status=200,
    )


@bp.route("/things/<int:id>", methods=["GET"])
def get(id) -> Response:
    """Get a thing"""
    thing = db.get_or_404(Thing, id)

    return Response(
        response=repr(thing),
        mimetype="application/json",
        status=200,
    )


@bp.route("/things/<int:id>", methods=["PUT"])
def update(id) -> Response:
    """Update a thing"""
    try:
        validate(instance=request.json, schema=thing_schema)
    except ValidationError as e:
        raise BadRequest(description=e.message)
    else:
        thing = db.get_or_404(Thing, id)
        thing.name = request.json["name"].title().strip()
        thing.colour = request.json["colour"]
        thing.quantity = request.json["quantity"]
        thing.updated_at = datetime.now(timezone.utc)
        db.session.add(thing)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise Conflict()
    except Exception:
        db.session.rollback()
        raise InternalServerError()
    else:
        return Response(
            response=repr(thing),
            mimetype="application/json",
            status=200,
        )


@bp.route("/things/<int:id>", methods=["DELETE"])
def delete(id) -> Response:
    """Delete a thing"""
    thing = db.get_or_404(Thing, id)
    db.session.delete(thing)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise InternalServerError()
    else:
        return Response(status=204)
    finally:
        db.session.close()


@bp.app_errorhandler(HTTPException)
def http_error(error):
    return Response(
        response=json.dumps(
            {"name": error.name, "description": error.description},
            separators=(",", ":"),
        ),
        mimetype="application/json",
        status=error.code,
    )


@bp.app_errorhandler(Exception)
def unhandled_exception(error):
    db.session.rollback()
    db.session.close()
    raise InternalServerError()
