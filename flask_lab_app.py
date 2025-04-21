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

if __name__ == "__main__":
    app.run()