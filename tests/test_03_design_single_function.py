from lib._03_design_single_function import *

def test_est_reading_time():
    result = est_reading_time(436)
    assert result == "This text will take around 2 minutes to read"
    result = est_reading_time(1745)
    assert result == "This text will take around 8 minutes to read"



def test_grammar_check():
    result = grammar_check("Hello sir!")
    assert result == True




def test_track_tasks():
    result = track_tasks("Shopping #TODO")
    assert result == True

    result1 = track_tasks("Clean up")
    assert result1 == False

    result2 = track_tasks("")
    assert result2 == False