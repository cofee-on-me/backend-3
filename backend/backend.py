from flask import jsonify, abort
from . import app


@app.route("/part/<part_id>")
def list_parts(part_id):
    parts = {
        "1": {"id": 1, "name": "jQuery is the king!"},
        "2": {"id": 2, "name": "jQuery is the lord!"},
        "3": {"id": 3, "name": "Some random message!"},
        "4": {"id": 4, "name": "Import jQuery!"},
        "5": {"id": 5, "name": "Please use jquery!"},
        "6": {"id": 6, "name": "Jquery is the lord!"},
    }

    if part_id not in parts.keys():
        abort(404)

    return jsonify(parts[part_id])
