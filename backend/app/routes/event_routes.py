from flask import request, jsonify, abort
from app.db import db
from app.models import Event

def init_event_routes(app):

    @app.route('/events', methods=['POST'])
    def create_event():
        description = request.json.get('description')
        if not description:
            abort(400, description="Description is required.")
        event = Event(description)
        db.session.add(event)
        db.session.commit()
        return jsonify(event.as_dict()), 201

    @app.route('/events', methods=['GET'])
    def get_all_events():
        events = Event.query.all()
        events_json = [event.as_dict() for event in events]
        return jsonify(events_json)

    @app.route('/events/<int:id>', methods=['GET'])
    def get_event_by_id(id: int):
        event = Event.query.get(id)
        if event is None:
            abort(404, description=f"Event with ID {id} not found.")
        return jsonify(event.as_dict())

    @app.route('/events/<int:id>', methods=['DELETE'])
    def delete_event(id: int):
        event = Event.query.get(id)
        if event is None:
            abort(404, description=f"Event with ID {id} not found.")
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": f"Deleted Event (id: {id})"}), 204

    @app.route('/events/<int:id>', methods=['PUT'])
    def update_event(id: int):
        event = Event.query.get(id)
        if event is None:
            abort(404, description=f"Event with ID {id} not found.")
        
        if not request.json:
            abort(400, description="No JSON data provided.")

        if 'description' in request.json:
            event.description = request.json['description']
        
        db.session.commit()
        return jsonify(event.as_dict())
