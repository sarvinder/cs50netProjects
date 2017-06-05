from flask import Flask,render_template

app=Flask(__name__)

@app.route('/home')
@app.route('/Home')
@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/Menues')
def Menues():
    return render_template('Menu.html')

@app.route('/party_to_go')
def party_to_go():
    return "This is party to go menu page"

@app.route('/corporate_menu')
def corporate_menu():
    return "THis is corporate menu page"

@app.route('/special_event_menu')
def special_event_menu():
    return "This is special event menu page"

@app.route('/News')
def News():
    return render_template('News.html')

@app.route('/Galery')
def Galery():
    return render_template('galery.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')
