from lib._03_design_single_function import *

def test_est_reading_time():
    result = est_reading_time(436)
    assert result == "This text will take around 2 minutes to read"
    result = est_reading_time(1745)
    assert result == "This text will take around 8 minutes to read"