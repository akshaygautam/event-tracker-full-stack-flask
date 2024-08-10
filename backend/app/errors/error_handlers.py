from flask import jsonify

def init_error_handlers(app):
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
