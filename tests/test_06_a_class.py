from lib._06_design_a_class import *

def test_add():
    tasklist = TaskList()
    result1 = tasklist.add("clean")
    assert result1 == [{"task": "clean", "completed": False}]
    result2 = tasklist.add("wash")
    assert result2 == [{"task": "clean", "completed": False}, {"task": "wash", "completed": False}]

def test_remove_task():
    tasklist = TaskList()
    tasklist.add("tidy")
    result = tasklist.remove_task("tidy")
    assert result == []

def mark_as_coomplete():
    tasklist = TaskList()
    import unittest


def test_mark_as_complete():
    task_list = TaskList()
    task_list.add("tidy")
    
    assert task_list.tasks == [{"task": "tidy", "completed": False}]
    result = task_list.mark_as_complete("tidy")
    assert result is True
    assert task_list.tasks == [{"task": "tidy", "completed": True}]






def test_add_track():
    musictracker = MusicTracker()
    result = musictracker.add_track("song 1")
    assert result == ["song 1"]
    result2 = musictracker.add_track("song 2")
    assert result2 == ["song 1", "song 2"]

def test_show_list():
    musictracker = MusicTracker()
    result = musictracker.show_list()
    assert result == []