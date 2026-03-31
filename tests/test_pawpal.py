from pawpal_system import Task, Pet


def test_toggle_complete():
    task = Task(description="Morning walk", duration=30, priority=1, due_time="07:00")
    assert task.completed is False
    task.toggle_complete()
    assert task.completed is True
    task.toggle_complete()
    assert task.completed is False


def test_add_task_increases_count():
    pet = Pet(name="Mochi", animal_type="dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="07:00"))
    assert len(pet.tasks) == 1
    pet.add_task(Task(description="Feeding", duration=10, priority=2, due_time="12:00"))
    assert len(pet.tasks) == 2
