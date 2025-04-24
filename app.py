from flask import Flask

app = Flask(__name__)

@app.route('/')
def this():
    return "fermented greenland shark"

if __name__ == "__main__":
    app.run()
