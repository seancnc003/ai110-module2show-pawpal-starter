from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="Jordan", time_available=120)

# Create pets
dog = Pet(name="Mochi", animal_type="dog")
cat = Pet(name="Whiskers", animal_type="cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks to pets
dog.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="07:00"))
dog.add_task(Task(description="Evening feeding", duration=10, priority=2, due_time="18:00"))
cat.add_task(Task(description="Litter box cleaning", duration=15, priority=1, due_time="08:00"))
cat.add_task(Task(description="Play time", duration=20, priority=3, due_time="12:00"))

# Generate and print schedule
scheduler = Scheduler(owner)
plan = scheduler.generate_plan()

print("=" * 40)
print("  Today's Schedule for", owner.name)
print("=" * 40)
print(scheduler.explain_plan(plan))
print("=" * 40)
