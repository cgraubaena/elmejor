from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hola'

if __name__== "__main__":
    app.run()