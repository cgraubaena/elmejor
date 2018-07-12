from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Mi primera página'

@app.route("/chau")
def home():
    return 'chauchauchauuuuu'



if __name__== "__main__":
    app.run()