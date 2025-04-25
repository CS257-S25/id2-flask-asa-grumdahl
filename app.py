from flask import Flask
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    with open ("./homepage.html") as f:
        homepage_local = f.read()
    return homepage_local

data = []

def load_data(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

"""
def load_all_data():
    load_data('Dummy_data/dummy_amazon.csv')

@app.route('/<row>/<column>', strict_slashes=False)
def get_cell(row,column):
    return data[int(row)][int(column)]

@app.errorhandler(404)
def page_not_found(e):
    return "Nothing leads here! I recommend navigating back to the homepage."

@app.errorhandler(500)
def python_bug(e):
    return "Some kind of bug happened..."
"""

if __name__ == "__main__":
    app.run()
