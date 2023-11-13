from uzwords import words
from difflib import get_close_matches


def word_check(msg):
    matches = get_close_matches(msg, words, 10)
    available = True if msg in matches else False
    return {"available": available, "matches": matches}
