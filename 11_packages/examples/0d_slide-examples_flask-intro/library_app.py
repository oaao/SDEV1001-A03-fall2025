import csv

from flask import jsonify, Flask

app = Flask(__name__)


@app.route("/")
def home():
	return "<h1>Welcome to the Book Library API!</h1>"


# in your terminal, making sure you're in the venv:
# 1. set an environment variable so flask knows what to run as an entrypoint
# 2. run the flask module directly and it will create the webserver
#
# set FLASK_APP=library_app.py
# flask run

# books = [
# 	{"title": "1984", "author": "George Orwell"},
# 	{"title": "To Kill a Mockingbird", "author": "Harper Lee"}
# ]


def load_books(filepath):

	books = []

	with open(filepath, mode="r", encoding="utf-8") as f:
		csv_reader = csv.DictReader(f)  # assumes the first row in CSV is fieldnames, not values
		for row in csv_reader:
			books.append(row)

	return books


@app.route("/books", methods=["GET"])
def get_books():
	books = load_books("data/books.csv")
	return jsonify(books)  # serialise our list of dicts into a JSON string
