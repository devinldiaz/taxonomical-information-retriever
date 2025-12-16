from streamlit.testing.v1 import AppTest

at = AppTest.from_file("pages/home.py").run()


def test_home_page_title():
    assert len(at.title) > 0
    assert "ParaSite" in at.title[0].value


def test_input():
    search = "Parasite not listed? Enter the scientific name & search here:"
    assert search in at.text_input[0].label


def test_search_button():
    assert "Search" in at.button[0].label
