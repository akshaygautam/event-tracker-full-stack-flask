from flask import request, jsonify, abort
from app.aiml import load_and_train_model, predict_object, generate_frequency_map
# Load the model when the application starts
model = load_and_train_model()

def init_aiml_routes(app):
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
        
    @app.route('/frequency-map', methods=['GET'])
    def get_frequency_map():
        frequency_map = generate_frequency_map(model)
        return jsonify(frequency_map)