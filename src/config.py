"""FLASK CONFIGURATION CLASS FILE"""


from distutils.debug import DEBUG


class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    DEBUG = True
