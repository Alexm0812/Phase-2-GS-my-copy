from lib._08_tdd_multi_class import *

"""def test_add_and_all():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents of entry1")
    entry2 =DiaryEntry("Title 2", "Contents of entry2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


def test_count_words():
    diary = Diary()
    entry = DiaryEntry("Sample Title", "This is a sample diary entry.")
    diary.add(entry)

    result = diary.count_words()
    assert result == entry.count_words()


def test_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Contents of entry1")
    entry2 = DiaryEntry("Title 2", "Contents of entry2")
    
    diary.add(entry1)
    diary.add(entry2)

    total_reading_time = diary.reading_time(100)
    
    assert total_reading_time == entry1.reading_time(100) + entry2.reading_time(100)

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "one two three")
    entry2 = DiaryEntry("Title 2", "one two three four five six seven")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1



def test_reading_chunk():
    entry1 = DiaryEntry("Title 1", "one two three")
    assert entry1.reading_chunk(2, 1) == "one two"
    



def test_add_todo():
    todolist = TodoList()
    entry1 = Todo("clean")
    result = todolist.add(entry1)
    assert entry1 in todolist.list
    
def test_incomplete():
    todolist = TodoList()
    entry1 = Todo("clean")
    entry2 = Todo("study")
    
    todolist.add(entry1)
    todolist.add(entry2)

    entry1.mark_complete()

    incomplete_todos = todolist.incomplete()
    assert entry1 not in incomplete_todos
    assert entry2 in incomplete_todos

def test_complete():
    todolist = TodoList()
    entry1 = Todo("work")
    entry2 = Todo("tidy")
    
    todolist.add(entry1)
    todolist.add(entry2)
    entry1.mark_complete()
    complete_todos = todolist.complete()
    assert entry1 in complete_todos
    assert entry2 not in complete_todos


def test_give_up():
    todolist = TodoList()
    entry1 = Todo("work")
    entry2 = Todo("tidy")
    todolist.add(entry1)
    todolist.add(entry2)
    
    # Check if the todos are initially not complete
    assert entry1.complete is False
    assert entry2.complete is False

    # Call give_up to mark all todos as complete
    todolist.give_up()

    # Check if the todos are marked as complete within todolist.list
    assert todolist.list[0].complete is True
    assert todolist.list[1].complete is True
"""



def test_add():
    todolist = TodoList()
    entry1 = Todo("clean")
    todolist.add(entry1)
    assert entry1 in todolist.list

def test_incomplete():
    todolist = TodoList()
    entry1 = Todo("clean")
    entry2 =  Todo("Tidy")
    todolist.add(entry1)
    todolist.add(entry2)
    entry1.mark_complete()
    incomplete_todo = todolist.incomplete()
    assert entry1 not in incomplete_todo
    assert entry2 in incomplete_todo

def test_give_up():
    todolist = TodoList()
    entry1 = Todo("clean")
    entry2 =  Todo("Tidy")
    todolist.add(entry1)
    todolist.add(entry2)
    giveup_todo = todolist.give_up()
    
    assert todolist.list[0].complete is True
    assert todolist.list[1].complete is True

