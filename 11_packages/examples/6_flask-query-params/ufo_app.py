import csv

from flask import Flask, request, jsonify


# you don't *need* to set a FLASK_APP environment variable.... you could also
# flask --app my_python_file run
#
# other flags include
# --debug  (error traceback on webpage if it crashes), and
# --reload (reloads pages automatically upon saved changes)


app = Flask(__name__)

# helper functions
def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings


# root page
@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>UFO Sightings</title>
      </head>
      <body>
        <h1>Welcome to the UFO Sightings API!</h1>
        <p>Use the <a href="/sightings">/sightings</a> endpoint route to get UFO sighting data.</p>
        <hr />
        <small>I WANT TO BELIEVE</small>
      </body>
    </html>
    """


# ufo endpoint
@app.route('/sightings', methods=['GET'])
def get_sightings():
    sightings = load_ufo_data('data/scrubbed.csv')
    return jsonify(sightings)
