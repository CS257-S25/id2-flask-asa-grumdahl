from flask import Flask
import csv

app = Flask(__name__)

@app.route('/')

def homepage():
    load_data()
    return "fermented greenland shark"

data = []
def load_data():
    with open('dataset.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

@app.route('/<row>/<column>', strict_slashes=False)
def get_cell(row,column):
    return data[int(row)][int(column)]

@app.errorhandler(404)
def page_not_found(e):
    return "there aint shit here try somewhere else"

@app.errorhandler(500)
def python_bug(e):
    return "i fucked up... sorry"


if __name__ == "__main__":
    app.run()