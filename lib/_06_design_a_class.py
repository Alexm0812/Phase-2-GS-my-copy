"""As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

class TaskList()
going to need a list for the tasks under __init__.

add function
this will add to do tasks to the list
can also return the list using this function. 

function to remove one done


"""

class TaskList():

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "completed": False})
        return self.tasks
    
    def mark_as_complete(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True
                return True
        return False



    def remove_task(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                self.tasks.remove(task)
                return self.tasks
        return self.tasks


"""As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

add a remove function.
use del to remove from list and then return reminader of list

"""""

    


tasklist = TaskList()
result = tasklist.add("clean")
result2 = tasklist.add("tidy")
result3 = tasklist.add("wash")
result3 = tasklist.mark_as_complete("tidy")
print(result)


"""As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

class MusicTracker()

__init__() - contain listened_tracks = [] contain a list of strings that will be the tracks

add_track (self, track)- these will be strings. the purpose will be to represent the track
this will add the track to the listened tracks list. 
return the list to show the user which tracks they have listened to .

"""

class MusicTracker():
    def __init__(self):
        self.listened_tracks = []
    
    def add_track(self, track):
        self.listened_tracks.append(track)
        return self.listened_tracks
    
    def show_list(self):
        return self.listened_tracks
music_tracker = MusicTracker()
music_tracker.add_track("song 1")
music_tracker.add_track("song 2")
print(music_tracker.listened_tracks)
music_tracker.add_track("song 3")
print(music_tracker.listened_tracks)
