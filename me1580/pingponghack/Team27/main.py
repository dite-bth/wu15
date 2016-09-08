# coding=utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")                                                         #Visar att detta är rootsidan.
def index():
    return "<h1> Välkommen till pingpong bamwamrang </h1>"                                                          #Här kan man lägga in url för att skicka till annan sida.

@app.route("/registrering_pingponghack")
def registrering_pingponghack():
    return render_template("registrering_pingponghack.html")
    
if __name__=="__main__":                                                 #ser till att servern startar när __name__ anropas.
    app.run (host='193.11.186.238', debug=True)                     #gör den public