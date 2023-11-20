

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
    






    #As a user
#So that I can improve my grammar
#I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.""""
    
def grammar_check(text):
    first = text[0]
    last = text[-1]
    special = "!"
    if first != first.upper():
        return False
    if not any(char in special for char in last):
        return False
    else:
        return True
    

#As a user
#So that I can keep track of my tasks
#I want to check if a text includes the string #TODO

""""" track_tasks = name of function
        text = paramenter

        return True or flase
        return true if it contains #TODO
use an if statemnt to see if it doent contain it
make a new variable that will contain the requiremnts
        

"""
def track_tasks(text):
    string = "#TODO"
    if not any(char in string for char in text):
        return False
    else:
        return True