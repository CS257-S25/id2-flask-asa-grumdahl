from flask import Flask
import csv
import re 

app = Flask(__name__)

@app.route('/')
def homepage():
    """ 
    Loads homepage.html as the site's home page. 
    """
    with open ("./homepage.html") as f:
        homepage_local = f.read()
    return homepage_local

def get_data(path_to_file):
    """ 
    Retrieves data given a filepath and returns it. 
        path_to_file: string representation of path to file
    """
    data = []
    with open(path_to_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def turn_dataset_name_in_url_to_filepath(dataset_name):
    """ 
    Turns the dataset name the user enters in the URL to a filepath. 
    """
    return "./Dummy_data/dummy_" + dataset_name.lower() + ".csv"


@app.route('/<dataset>/<movienum>', strict_slashes=False)
def dataset_page(dataset,movienum):
    """ 
    Generates a page for each dataset based on the info in the dataset. 
        dataset: name of the dataset to attempt to grab. throws 503 if not one of "amazon" "disney" "hulu" or "netfix"
        movienum: number inside dataset to grab
    """
    data = get_data(turn_dataset_name_in_url_to_filepath(dataset))
    return data[int(movienum)][4]

@app.errorhandler(404)
def  page_not_found(e):
    return "There's nothing here! Try returning to the main page."

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
