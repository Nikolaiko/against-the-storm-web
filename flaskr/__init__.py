from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DATABASE'] = 'sqlite3.db'

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
    
    @app.route("/resources/fabric")
    def display_fabric():
        return render_template("resources/fabric_page.html")

    return app