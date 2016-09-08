# coding=utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")                                                         #Visar att detta är rootsidan.
def index():
    return "?"                                                          #Här kan man lägga in url för att skicka till annan sida.

@app.route("/registrering_pingponghack")
def registrering_pingponghack():
    return render_templates("registrering_pingponghack.html")
    
if __name__=="__main__":                                                 #ser till att servern startar när __name__ anropas.
    app.run (host='193.11.186.238', PORT = 5000, debug=True)                     #gör den public