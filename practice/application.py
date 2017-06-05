from flask import Flask,render_template,jsonify, url_for
from flask_jsglue import JSGlue
app=Flask(__name__)
JSGlue(app)
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/name")
def givename():
    
    return jsonify(name= "savi")