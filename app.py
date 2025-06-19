from flask import Flask
from flask_pymongo import PyMongo
from flasgger import Swagger
import os

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def health_check():
        return "Flask app is running!", 200

    # Config Load
    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        from config.prod_config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config.dev_config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    mongo.init_app(app)
    app.config['MONGO_CLIENT'] = mongo.cx

    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "Inventory API",
            "description": "CRUD API",
            "version": "1.0"
        },
        "basePath": "/",
        "schemes": ["http"]
    })

    # Register blueprints
    from controllers.inventory_controller import inventory_bp
    app.register_blueprint(inventory_bp)

    return app
