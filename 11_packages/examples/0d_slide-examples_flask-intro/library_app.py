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

books = [
	{"title": "1984", "author": "George Orwell"},
	{"title": "To Kill a Mockingbird", "author": "Harper Lee"}
]


@app.route("/books")
def get_books():
	return jsonify(books)  # serialise our list of dicts into a JSON string
