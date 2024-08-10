from .event_routes import init_event_routes
from .app_routes import init_app_routes

def init_routes(app):
    init_app_routes(app)
    init_event_routes(app)
