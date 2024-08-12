from flask import request, jsonify, abort
from aiml.RockVsMines import load_and_train_model, predict_object
# Load the model when the application starts
model = load_and_train_model()

def init_event_routes(app):
    @app.route('/mlquery/<term>', methods=['POST'])
    def ml_query(term):
        try:
            # Convert the input term to a tuple of floats
            input_data = tuple(map(float, term.split(',')))
            
            # Call the prediction function
            result = predict_object(model, input_data)
            
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400