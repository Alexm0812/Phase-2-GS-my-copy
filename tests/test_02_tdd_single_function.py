from lib._02_tdd_single_function import *

def test_make_snippet():
    result = make_snippet("hello bye hello bye hello bye hello")
    assert result == "hello bye hello bye hello ..."
    result = make_snippet("hello bye hello")
    assert result == "hello bye hello"

def test_count_words():
    result = count_words("hello bye hello")
    assert result == 3
    result = count_words("hello bye hello bye hello bye hello")
    assert result == 7
    