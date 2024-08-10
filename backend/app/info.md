your-project/
│
├── app/
│   ├── __init__.py              # Initializes the Flask app and imports necessary modules
│   ├── config/                  # Contains configuration files
│   │   ├── __init__.py          # Initializes the config package
│   │   ├── config.py            # Configuration settings
│   ├── db.py                    # Contains the SQLAlchemy instance
│   ├── models/                  # Contains model definitions
│   │   ├── __init__.py          # Initializes the models package
│   │   ├── event.py             # Event model
│   ├── routes/                  # Contains route handlers
│   │   ├── __init__.py          # Initializes the routes package and imports route modules
│   │   ├── event_routes.py      # Event-specific routes
│   ├── errors/                  # Contains error handlers
│   │   ├── __init__.py          # Initializes the errors package
│   │   ├── error_handlers.py    # Error handlers
│
├── frontend/                    # Frontend build files
│   ├── build/
│   │   ├── static/
│   │   ├── index.html
│
└── run.py                       # Entry point for running the application
