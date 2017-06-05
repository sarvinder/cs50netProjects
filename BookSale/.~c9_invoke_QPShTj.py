from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html')
@app.route('/Buy')
def Buy():
    return render_template('home.html')
@app.route('/Sell')
def Sell():
    return render_template('home.html')
    
