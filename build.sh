#!/bin/bash
python setup.py bdist_wheel

rm dist/Flask_blueprint_boilerplate-1.0.0-py3.9.egg

echo "build is available in dist folder"