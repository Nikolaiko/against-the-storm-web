from flask import Flask
from flask import render_template
from flask import abort

import requests
import json

#from model.resource_types import GameResource
from .model.resource_consts import *

from .utils.mapping_functions import *
from .model.resource_types import GameResource

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DATABASE'] = 'sqlite3.db'

    from . import db
    db.init_app(app)

    @app.route("/test")
    def test():
        result = json.loads(requests.get("http://127.0.0.1:8080/resources").text)
        return render_template("test.html", testResults = result)

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/creatures")
    def display_creatures_list():
        return render_template("creatures/creatures_list.html")

    @app.route("/resources")
    def display_resources_list():
        result = json.loads(requests.get("http://127.0.0.1:8080/resources").text)
        return render_template(
            "resources/resources_list.html",
            gameResources = result
        )
    
    @app.route("/resources/<string:res_name>")
    def display_resource(res_name):
        resource = json.loads(requests.get("http://127.0.0.1:8080/resources/" + res_name).text)
        return render_template(
            "resources/resource_page.html",
            name = resource["name"],
            title_name = resource["name"],
            image_url = resource["imageUrl"],
            desc = resource["description"]
        )
    
    return app
