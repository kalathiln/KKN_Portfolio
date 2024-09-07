from flask import Flask, render_template, request
from dotenv import load_dotenv
# This is used to load environmanet variables from the .env file during deploytment.
load_dotenv()

projects = [
    
    {
        "name" : "Photography in Abstract",
        "thumb": "/img/headshot.png",
        "hero": "",
        "categories":["Abstract","Portrait", "Landscape"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Germany",
        "thumb": "/img/germany_subway.png",
        "hero": "",
        "categories":["Landscape","Wald" , "subway" ],
        "slug": "germany",
        "prod": "https://udemy.com",
    },
    {
        "name" : "India",
        "thumb": "/img/nandi_temple.png",
        "hero": "",
        "categories":["India","landscape"],
        "slug": "api-docs",
        "prod": "https://udemy.com",
    }

]

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"] )
    def home():
        return render_template("home.html", projects = projects)
    
    @app.route("/about", methods=["GET", "POST"])
    def about():
        return render_template("about.html")
    
    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    return app
