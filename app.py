from flask import Flask, jsonify
from server.config import BaseConfig

__all__ = ['create_app']


def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = __name__

    app = Flask(app_name)
    configure_app(app, config)
    configure_blueprints(app)
    configure_errorhandler(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(BaseConfig)
    if config:
        app.config.from_object(config)


def configure_blueprints(app):
    from server.views import bp_task
    app.register_blueprint(bp_task)



def configure_errorhandler(app):
    @app.errorhandler(Exception)
    def exception_error(error: Exception):
        return jsonify({'error': str(error), 'code': 500}), 500

from dotenv import load_dotenv
load_dotenv()

app = create_app()
app.run()