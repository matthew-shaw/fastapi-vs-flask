import json
from datetime import datetime, timezone

from app import db
from app.models import Thing
from app.thing import bp
from jsonschema import ValidationError, validate
from sqlalchemy.exc import IntegrityError

from flask import Response, request, url_for

# JSON schema for validation
with open("openapi.json") as json_file:
    openapi = json.load(json_file)
thing_schema = openapi["components"]["schemas"]["ThingRequest"]


@bp.route("/things", methods=["POST"])
def create_thing() -> Response:
    """Create a Thing"""

    try:
        validate(instance=request.json, schema=thing_schema)
    except ValidationError as e:
        error = {"message": e.message}
        return Response(
            response=json.dumps(error, separators=(",", ":")),
            mimetype="application/json",
            status=400,
        )
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
        return Response(status=409)
    except Exception:
        db.session.rollback()
        return Response(status=500)
    else:
        response = Response(
            response=repr(thing),
            mimetype="application/json",
            status=201,
        )

        response.headers["Location"] = url_for("thing.get_thing", id=thing.id)
        return response
    finally:
        db.session.close()


@bp.route("/things", methods=["GET"])
def list_things() -> Response:
    """Retrieve a list of Things"""
    things = [thing.as_dict() for thing in db.session.execute(db.select(Thing).order_by(Thing.created_at)).scalars()]

    return Response(
        response=json.dumps(things, separators=(",", ":")),
        mimetype="application/json",
        status=200,
    )


@bp.route("/things/<int:id>", methods=["GET"])
def get_thing(id) -> Response:
    """Retrive a thing"""
    thing = db.get_or_404(Thing, id)

    return Response(
        response=repr(thing),
        mimetype="application/json",
        status=200,
    )


@bp.route("/things/<int:id>", methods=["PUT"])
def update_thing(id) -> Response:
    """Update a thing"""
    try:
        validate(instance=request.json, schema=thing_schema)
    except ValidationError as e:
        error = {"message": e.message}
        return Response(
            response=json.dumps(error, separators=(",", ":")),
            mimetype="application/json",
            status=400,
        )
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
        return Response(status=409)
    except Exception:
        db.session.rollback()
        return Response(status=500)
    else:
        return Response(
            response=repr(thing),
            mimetype="application/json",
            status=200,
        )


@bp.route("/things/<int:id>", methods=["DELETE"])
def delete_thing(id) -> Response:
    """Delete a thing"""
    thing = db.get_or_404(Thing, id)
    db.session.delete(thing)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return Response(status=500)
    else:
        return Response(status=204)
    finally:
        db.session.close()
