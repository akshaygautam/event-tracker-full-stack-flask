from flask import Flask, request, render_template, send_from_directory, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

DATABASE_URI = 'postgresql://postgres:admin@localhost/baby-tracker'


app = Flask(__name__, static_folder="../frontend/build/static", template_folder="../frontend/build")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(100), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f'Event = {self.description}'
    
    def __init__(self, description) -> None:
        self.description = description

    def as_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

@app.route('/')
def serve():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/events',methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return jsonify(event.as_dict)


@app.route('/events', methods=['GET'])
def get_all_events():
    events = Event.query.all()
    events_json = [event.as_dict() for event in events]
    return jsonify(events_json)

@app.route('/events/<id>',methods=['GET'])
def get_event_by_id(id:int):
    event = Event.query.get(id)
    if event is None:
        abort(404, description=f"Event with ID {id} not found.")
    return jsonify(event.as_dict())


@app.route('/events/<id>',methods=['DELETE'])
def delete_event(id:int):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return f'Deleted Event (id: {id})'

@app.route('/events/<id>',methods=['PUT'])
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

if __name__ == '__main__':
    app.run()


@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not Found', 'message': error.description})
    response.status_code = 404
    return response

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred. Please try again later.'})
    response.status_code = 500
    return response