from flask import request, render_template

def init_app_routes(app):
    @app.route('/')
    def serve():
        return render_template('index.html')
    