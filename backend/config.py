from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import os

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://?mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Serve static files from the "dist" folder under the frontend dir 
@app.route("/", defaults = {"filename": ""})
@app.route('/<path:filename>')
def method_name():
    if not filename:
        filename = "index.html"
        return send_from_directory(dist_floder, filename)

# api routes

db = SQLAlchemy(app)