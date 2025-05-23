"""
app.py

This runs a small application using some of the backend data coded for my team project.
Features are described in homepage.html.
"""

from flask import Flask, request
from ProductionCode import data as datapy
from ProductionCode import filter as filterpy

app = Flask(__name__)

@app.route('/')
def homepage():
    """ 
    Loads homepage.html as the site's home page.
    """
    with open ("./homepage.html", encoding="utf_8") as f:
        homepage_local = f.read()
    return homepage_local

@app.route('/filter',strict_slashes=False)
def filter_page():
    """
    Loads a page visualizing a filtered dataset.
    """
    initialize_data()
    release_year_onward = parse_ui_release_year_onward(request.args.get("ry"))
    filterpy.Filter.filter_by_year_onward(filterpy.Filter,release_year_onward)
    return str(filterpy.Filter.get_filtered_media_dict(filterpy.Filter))

def initialize_data():
    """
    Initializes the data for rendering in the website.
    """
    datapy.Data.__init__(datapy.Data)
    filterpy.Filter.__init__(filterpy.Filter, datapy.Data)

def parse_ui_release_year_onward(ui_ry):
    """
    Parses user input for a release year, so it may be read by filter.py's 
    functions. Returns a catch-all year otherwise.
    """
    try:
        return int(ui_ry)
    except:
        return 0

@app.errorhandler(404)
def page_not_found(Exception e):
    """
    Placeholder 404 page.
    """
    print(e)
    return "There's nothing here! Try returning to the main page."

if __name__ == "__main__":
    app.run()
