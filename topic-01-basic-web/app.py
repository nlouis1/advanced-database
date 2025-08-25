from flask import Flask

#, render_template, request, redirect, url_for
# import sqlite3

# remember to $ pip install flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_index():
    return "Hello from the flask server."

