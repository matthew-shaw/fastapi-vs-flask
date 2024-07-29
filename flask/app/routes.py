import json

from app import app, db
from app.models import Thing
from sqlalchemy.exc import IntegrityError

from flask import Response, request


@app.route("/v1/things", methods=["POST"])
def create_thing():
    """Create a Thing"""
    thing = Thing(
        name=request.json["name"],
        colour=request.json["colour"],
        quantity=request.json["quantity"],
    )

    db.session.add(thing)

    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return Response(status=400)
    except Exception:
        db.session.rollback()
        return Response(status=500)
    else:
        response = Response(
            response=repr(thing),
            mimetype="application/json",
            status=201,
        )

        response.headers["Location"] = f"{request.url}/{thing.id}"
        return response
    finally:
        db.session.close()


@app.route("/v1/things", methods=["GET"])
def list_things():
    """Retrieve a list of Things"""
    things = [thing.as_dict() for thing in db.session.execute(db.select(Thing).order_by(Thing.created_at)).scalars()]

    return Response(
        response=json.dumps(things, separators=(",", ":")),
        mimetype="application/json",
        status=200,
    )
