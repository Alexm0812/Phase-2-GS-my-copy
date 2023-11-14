

"""
EX1: 

Returns: estimated reading time.

Parameter: text -> convert to words 

divide by 200 


"""

def est_reading_time(text):
    """
    parameters: no. of words in text -> divide by 200 -> convert float to int 
    returns: time -> minutes
    side effects: None
    """
    est_wpm = int(text / 200)
    return f"This text will take around {est_wpm} minutes to read"
    