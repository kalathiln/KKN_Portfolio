from flask import Flask, render_template, request, abort
from dotenv import load_dotenv
# This is used to load environmanet variables from the .env file during deploytment.
load_dotenv()

projects = [
    
    {
        "name" : "Photography in Abstract",
        "thumb": "/img/headshot.png",
        "hero": "",
        "categories":["Abstract","Portrait", "Landscape"],
        "slug": "abstract-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Germany",
        "thumb": "/img/germany_subway.png",
        "hero": "",
        "categories":["Landscape","Wald" , "subway" ],
        "slug": "germany-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "India",
        "thumb": "/img/nandi_temple.png",
        "hero": "",
        "categories":["India","people", "culture"],
        "slug": "india-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Shop",
        "thumb": "/img/giraffe_small.png",
        "hero": "",
        "categories":["K&K", "Ganesha", "Psylosphy"],
        "slug": "myshop",
        "prod": "https://www.redbubble.com/de/shop/ap/162571374?asc=u",
    }

    

]

slug_to_project = {project["slug"]:project for project in projects}

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
    
    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)

        # return render_template("project_"+slug+".html")
        return render_template(f"{slug}.html",
                               project=slug_to_project[slug])
        
    return app
