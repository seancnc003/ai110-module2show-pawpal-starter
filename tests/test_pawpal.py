from pawpal_system import Task, Pet, Owner, Scheduler


def test_toggle_complete():
    task = Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00")
    assert task.completed is False
    task.toggle_complete()
    assert task.completed is True
    task.toggle_complete()
    assert task.completed is False


def test_add_task_increases_count():
    pet = Pet(name="Mochi", animal_type="dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00"))
    assert len(pet.tasks) == 1
    pet.add_task(Task(description="Feeding", duration=10, priority=2, due_time="2026-03-31 12:00"))
    assert len(pet.tasks) == 2


def test_sorting_correctness():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", animal_type="dog")
    owner.add_pet(pet)
    pet.add_task(Task(description="Evening feeding", duration=10, priority=2, due_time="2026-03-31 18:00"))
    pet.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00"))
    pet.add_task(Task(description="Lunch check", duration=5, priority=3, due_time="2026-03-31 12:00"))
    scheduler = Scheduler(owner)
    plan = scheduler.generate_plan()
    assert plan[0].description == "Morning walk"
    assert plan[1].description == "Lunch check"
    assert plan[2].description == "Evening feeding"


def test_recurring_daily_task():
    task = Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00", frequency="daily")
    task.toggle_complete()
    assert task.due_time == "2026-04-01 07:00"
    assert task.completed is False


def test_conflict_detection_overlap():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", animal_type="dog")
    owner.add_pet(pet)
    pet.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00"))
    pet.add_task(Task(description="Vet visit", duration=60, priority=1, due_time="2026-03-31 07:15"))
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1
    assert "Morning walk" in conflicts[0]
    assert "Vet visit" in conflicts[0]


def test_pet_with_no_tasks():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", animal_type="dog")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    plan = scheduler.generate_plan()
    assert plan == []


def test_filter_by_pet():
    owner = Owner(name="Jordan")
    dog = Pet(name="Mochi", animal_type="dog")
    cat = Pet(name="Whiskers", animal_type="cat")
    owner.add_pet(dog)
    owner.add_pet(cat)
    dog.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00"))
    cat.add_task(Task(description="Litter box", duration=15, priority=1, due_time="2026-03-31 08:00"))
    scheduler = Scheduler(owner)
    mochi_tasks = scheduler.filter_by_pet("Mochi")
    assert len(mochi_tasks) == 1
    assert mochi_tasks[0].description == "Morning walk"


def test_exact_same_time_conflict():
    owner = Owner(name="Jordan")
    dog = Pet(name="Mochi", animal_type="dog")
    cat = Pet(name="Whiskers", animal_type="cat")
    owner.add_pet(dog)
    owner.add_pet(cat)
    dog.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00"))
    cat.add_task(Task(description="Litter box", duration=15, priority=1, due_time="2026-03-31 07:00"))
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1
