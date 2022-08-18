"""
    will hold application main file
"""
import flask
import flask_restful

from .config import Config
from .simple_api.hello_api import Hello_BP


def create_app() -> flask.Flask:
    """
    create flask application
    return: a flask application
    rtype: flask.Flask
    """

    app = flask.Flask(__name__)
    app.config.from_object(Config)
    url_prefix = "/hello"
    app.register_blueprint(Hello_BP, url_prefix=url_prefix)

    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(412)
    @app.errorhandler(422)
    def handle_error(error):
        headers = getattr(error, 'data', {}).get('headers')
        return flask.Response(status=error.code,
                              headers=headers)

    return app