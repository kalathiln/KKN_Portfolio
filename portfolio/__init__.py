from flask import Flask, render_template, request
from dotenv import load_dotenv
# This is used to load environmanet variables from the .env file during deploytment.
load_dotenv()

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"])
    def home():
        return render_template("home.html")
    
    @app.route("/about", methods=["GET", "POST"])
    def about():
        return render_template("about.html")
    
    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    return app
