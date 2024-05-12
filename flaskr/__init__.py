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

    result = json.loads(requests.get("http://127.0.0.1:8080/resources").text)
    print(result[0])

    from . import db
    db.init_app(app)

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/creatures")
    def display_creatures_list():
        return render_template("creatures/creatures_list.html")

    @app.route("/resources")
    def display_resources_list():
        return render_template("resources/resources_list.html")
    
    @app.route("/resources/brick")
    def display_brick():
        return render_template("resources/brick_page.html")
    
    #@app.route("/resources/fabric")
    #def display_fabric():
    #    return render_template("resources/fabric_page.html")
    
    @app.route("/resources/<string:res_name>")
    def display_resource(res_name):
   #     res = json.loads(requests.get('http://127.0.0.1:8080/readers').text)
   #     print(res[0]["phone"])
        resource = getResFromName(res_name)
        if resource == None:
            abort(404)
        return render_template(
            "resources/resource_page.html",
            name = resource.name,
            title_name = resource.titleName,
            image_url = resource.imageUrl,
            desc = resource.description
        )
    return app
