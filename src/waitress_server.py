# pylint: disable=protected-access
import click
import waitress
from paste.translogger import TransLogger
from werkzeug.middleware.proxy_fix import ProxyFix

from . import app, deploy


def waitress_server(port=5001, *, host='0.0.0.0'):
    """Creates dynamodb tables and then serves app through waitress
    :param port: int, server port
    :param host: str, server host
    """
    flask_app_ = app.create_app()
    flask_app_.wsgi_app = ProxyFix(flask_app_.wsgi_app)
    flask_app_ = TransLogger(flask_app_, setup_console_handler=True)
    waitress.serve(
        flask_app_,
        host=host,
        port=port,
        _quiet=True,
        url_prefix="/api",
    )


@deploy.command("waitress")
@click.option(
    "--port",
    help="Port to listen on.",
    type=int,
    default=5001,
)
def _waitress(port):
    """A waitress entry point to the m2a-tv2-api module."""
    waitress_server(port)


if __name__ == '__main__':
    _waitress()