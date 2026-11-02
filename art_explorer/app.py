# Import Flask tools needed to create the app, display HTML pages,
# and get information submitted through the search form.
from flask import Flask, render_template, request

# Import requests to handle API request errors.
import requests

# Import the search function from api.py.
from .api import search_artworks

# Create the Flask application.
app = Flask(__name__)


# Route for the home page (/)
# - When someone visits the home page:
#   - Display the home.html template.
#   - Show the search form.
@app.route("/")
def home():
    return render_template("home.html")


# Route for the search results page (/results)
# - Get the search term submitted through the search form.
# - Check whether the search term is empty.
#   - If it is empty, display a message asking the user to enter a search term.
# - If a search term was entered:
#   - Call the API search function using the search term.
#   - Get the list of matching artworks.
#   - If artworks are found, display the results.
#   - If no artworks are found, display a no-results message.
#   - If the API request fails, display an error message.
# - Pass the search term and artwork results to results.html.
@app.route("/results")
def results():
    search_term = request.args.get("search", "")

    # Check whether the search term is empty.
    if search_term.strip() == "":
        return render_template(
            "results.html",
            search_term=search_term,
            artworks=[],
            error_message=""
        )

    # Search the Art Institute API for matching artworks.
    try:
        artworks = search_artworks(search_term)
        error_message = ""

    # Handle problems with the API request.
    except requests.exceptions.RequestException:
        artworks = []
        error_message = (
            "Unable to connect to the Art Institute API. Please try again."
        )

    # Display the search results.
    return render_template(
        "results.html",
        search_term=search_term,
        artworks=artworks,
        error_message=error_message
    )


# Start the Flask application when this file is run directly.