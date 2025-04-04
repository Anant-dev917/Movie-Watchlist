from flask import Flask, render_template
import os
from movie_library.routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def create_app():

    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY","Perugia")

    #The MongoClient instance will be stored in the 'db' property of app (Also, refer to "app.py" in Habit Tracker project)
    app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()

    app.register_blueprint(pages)

    return app