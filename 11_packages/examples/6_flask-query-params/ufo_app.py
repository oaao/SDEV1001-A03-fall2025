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
    """Test with e.g. localhost:5000/sightings?country=ca"""

    # in flask, the request that lands on your endpoint is something you have access to *implicitly*
    # by importing the request object & inspecting it here!
    # import pprint
    # pprint.pprint(         # built-in pretty-print module, letting us do nicely formatted printing
    #     request.__dict__,  # obj.__dict__ dumps an object/instance out as a dictionary of the data it holds
    #     indent=2
    # )
    # print(request.args)
    # ... or, use breakpoint() to inspect the request object!!!
    
    sightings = load_ufo_data('data/scrubbed.csv')  # this is a list of dictionaries, where each sighting is a dict

    country = request.args.get('country', '')  # allow filtration by a ?country={country_code} URLparam

    # we could loop through the list of dicts and remove anything that doesn't match the filter, or...
    # just write a list expression!
    if country:
        sightings = [
            sighting for sighting in sightings if sighting['country'].lower() == country
        ]

    return jsonify(sightings)
