"""WSGI entry point for the module."""
import logging
import pathlib

import click

log = logging.getLogger(__name__)

LOG_FORMAT_SIMPLE = "{asctime} {levelname} {message}"
LOG_FORMAT_VERBOSE = (
    "{asctime} {levelname} {processName}"
    " {threadName} {name} {pathname}:{lineno}: {message}"
)


class Path(click.Path):
    """Path wrapper for Click path type.

    Normally, :class:`click.Path` parameter type returns a unicode
    string of a path. This custom type extends the parameter type so
    that the string path wrapped in  a :class:`pathlib.Path` before
    being returned.

    When a dash is given and ``allow_dash`` is enabled, the returned
    path will point to the stdin file descripter in /proc.
    """

    def convert(self, value, parameter, context):  # pylint: disable=arguments-differ
        converted = super().convert(value, parameter, context)
        if self.allow_dash and converted == "-":
            converted = "/proc/{pid}/fd/0".format(pid=os.getpid())
        return pathlib.Path(converted)


class ClickLogHandler(logging.Handler):
    """Log handler based off of Click.

    This handler uses :func:`click.echo` to emit log records. This
    means that it's safe to use colours and styling, e.g. via
    :func:`click.style`, in formatted log messages.

    All log records are emitted to stderr.
    """

    def emit(self, record):
        try:
            click.echo(self.format(record), err=True)
        except Exception:  # pylint: disable=broad-except
            self.handleError(record)


@click.group()
@click.option(
    "--log-level",
    type=click.Choice([logging.getLevelName(level).lower() for level in [
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    ]]),
    default="info",
    show_default=True,
    help="Only show logs at or above this level.",
)
@click.option(
    "--log-verbose",
    is_flag=True,
    help="Use a very noisy log format.",
)
@click.pass_context
def simple_api(context, log_level, log_verbose):
    log_formatter = logging.Formatter(
        LOG_FORMAT_SIMPLE, "%H:%M:%S", style="{")
    if log_verbose:
        log_formatter = logging.Formatter(LOG_FORMAT_VERBOSE, style="{")
    log_handler = ClickLogHandler()
    log_handler.setFormatter(log_formatter)
    log_root = logging.getLogger()
    log_root.setLevel(log_level.upper())
    log_root.addHandler(log_handler)


command = simple_api.command
group = simple_api.group