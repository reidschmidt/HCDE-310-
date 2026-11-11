
# HW5 test_app.py: tests for the artist search app.
# Run from this folder: python -m pytest

from app import app


def test_home_shows_search_form():
    client = app.test_client()
    page = client.get("/")
    assert page.status_code == 200
    assert b"Artist name" in page.data


def test_search_shows_artworks(monkeypatch):
    def fake_get_artworks(artist):
        return [
            {
                "title": "Water Lilies",
                "date_display": "1906",
                "image_id": "abc123"
            }
        ]

    monkeypatch.setattr("app.get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b"Water Lilies" in page.data
    assert b"1906" in page.data


def test_missing_image_shows_message(monkeypatch):
    def fake_get_artworks(artist):
        return [
            {
                "title": "Unknown Painting",
                "date_display": "1900",
                "image_id": None
            }
        ]

    monkeypatch.setattr("app.get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b"No image available" in page.data
