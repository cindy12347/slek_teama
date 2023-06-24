from os import path
from pathlib import Path

from flask import Flask, render_template, request
from flask_frozen import Freezer


template_folder = path.abspath('./templates')

app = Flask(__name__, template_folder=template_folder)
#app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page>')
def pages(page):
    return render_template(page.lower() + '.html')

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    freezer.freeze()
    app.run(port=9090, debug=True)
    