from .event_routes import init_event_routes
from .app_routes import init_app_routes
from .student_routes  import init_student_routes
from .aiml_routes import init_aiml_routes

def init_routes(app):
    init_app_routes(app)
    init_event_routes(app)
    init_student_routes(app)
    init_aiml_routes(app)
