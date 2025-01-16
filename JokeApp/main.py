from flask import Flask
import pyjokes

app = Flask(__name__)

@app.route("/")
def home():
    joke = pyjokes.get_joke()
    return f'<h2>{joke}</h2>'

@app.route("/MultipleJokes")
def jokes():
    joke_list = pyjokes.get_jokes()
    return f'<h2>{joke_list}</h2>'

if __name__ == '__main__':
    app.debug = True
    app.run()
