from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route('/')
def homesellstuff():
    return render_template("layout.html")
    
@app.route('/home')
def Home():
    return render_template('index.html')
@app.route('/Buy')
def Buy():
    return render_template('buy.html')
@app.route('/Sell')
def Sell():
    return render_template('sell.html')

@app.route("/recent_purchases")
def recent_purchases():
    return render_template("recent_purchases.html")
    
@app.route('/calculate')
def cal():
    firstname = "savi"
    lastname = "singh"
    lists=[firstname,lastname]
    return jsonify(lists)
    