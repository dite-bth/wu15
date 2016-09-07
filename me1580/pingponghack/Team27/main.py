from flask import flask

app = Flask(__name__)

@app.route("/")                         #Visar att detta är rootsidan.
def index():
    return "?"                          #Här kan man lägga in url för att skicka till annan sida.

if __name__="__main__":                 #ser till att servern startar när __name__ anropas.
    app.run(debug=True)