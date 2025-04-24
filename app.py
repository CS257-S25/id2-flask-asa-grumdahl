from flask import Flask

app = Flask(__name__)

@app.route('/')
def this():
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
    return "Nothing leads here! I recommend navigating back to the homepage."

@app.errorhandler(500)
def python_bug(e):
    return "Some kind of bug happened..."

if __name__ == "__main__":
    app.run()
