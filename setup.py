"""Set up script for the m2a-tv2-api package."""

import pathlib

import setuptools
import toml

PATH_ROOT = pathlib.Path(__file__).parent


def long_description():
    """Load the README."""
    with (PATH_ROOT / "README.md").open() as readme:
        return readme.read()


def get_install_requirements():
    try:
        # read my pipfile
        with open('Pipfile', 'r') as fh:
            pipfile = fh.read()
        # parse the toml
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []
    # if the package's key isn't there then just return an empty list
    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []
    # If a version/range is specified in the Pipfile honor it
    # otherwise just list the package
    return ["{0}{1}".format(pkg, ver) if ver != "*"
            else pkg for pkg, ver in required_packages]


def version():
    """
    flask blue print boilerplate for quick start
    so that satej can start any project as quick as possible with flask
    """
    return "1.0.0"


setuptools.setup(
    name="Flask-blueprint-boilerplate",
    version=version(),
    author="  satej sarker",
    description=long_description(),
    packages=setuptools.find_packages(exclude=['*.pyc', 'test']),
    entry_points={
        "console_scripts": [
            "simple-api=src:api",
        ],
    },
    install_requires=get_install_requirements(),
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9"
    ],
)