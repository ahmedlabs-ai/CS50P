from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AEIOU") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("hello") == "hll"