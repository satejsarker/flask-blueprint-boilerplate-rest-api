from crypt import methods
import logging

import flask_restful
from flask import Blueprint
from flask.views import MethodView

Hello_BP=Blueprint('hello_world',__name__)
API=flask_restful.Api(Hello_BP)

@API.resource( '/hello_world', strict_slashes=False, methods=["GET"])
class HelloApi(MethodView):
    def get(self):

        return {"hello":"Blue print world"} 
    
    