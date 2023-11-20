from lib._05_tdd_class import *
import pytest

def test_format():
    diary_entry = DiaryEntry("My Title",  "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

def test_count_words():
    diary_entry = DiaryEntry("My Title",  "These are the contents")
    result = diary_entry.count_words()
    assert result == 6 

def test_reading_time():
    with pytest.raises(Exception) as e:
        str(e.value)
    diary_entry = DiaryEntry("My Title",  "These are the contents")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_chunk():
    grammar = GrammarStats()
    
    result = grammar.check("text begins with a capital letter and ends with")
    assert result == False



def test_reading_chunk_called_twice():
    diary_entry = DiaryEntry("My Title",  "These are the contents")
    result1 = diary_entry.reading_chunk(2, 1)
    result2 = diary_entry.reading_chunk(2, 1)
    assert result1 == "These are"
    assert result2 == "the contents"



    #2 (Challenge)


def test_check():
    grammar = GrammarStats()
    
    result = grammar.check("Text begins with a capital letter and ends with!")
    assert result == True

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("This is a dog.")
    grammar_stats.check("This is a cat")
    grammar_stats.check("This is a mouse")
    
    result = grammar_stats.percetage_good()
    assert result == 33