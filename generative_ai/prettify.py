import cssbeautifier
import jsbeautifier
from bs4 import BeautifulSoup


def prettify_css(text):
    return cssbeautifier.beautify(text)


def prettify_javascript(text):
    return jsbeautifier.beautify(text)


def prettify_html(text):
    soup = BeautifulSoup(text, "html.parser")
    formatted_html = soup.prettify()
    return formatted_html


def prettify_text(text, file_type):
    prettify_options = {
        "css": prettify_css,
        "js": prettify_javascript,
        "html": prettify_html,
    }
    return prettify_options[file_type](text)
