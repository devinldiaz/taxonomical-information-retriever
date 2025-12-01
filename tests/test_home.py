from streamlit.testing.v1 import AppTest

at = AppTest.from_file("home.py").run()


def test_home_page_title():
    assert len(at.title) > 0
    assert "Taxonomical Information Retriever" in at.title[0].value


def test_input():
    search_text = "Enter the scientific name of an organism:"
    assert search_text in at.text_input[0].label


def test_search_button():
    assert "Search" in at.button[0].label
