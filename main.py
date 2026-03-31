from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="Jordan", time_available=120)

# Create pets
dog = Pet(name="Mochi", animal_type="dog")
cat = Pet(name="Whiskers", animal_type="cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks OUT OF ORDER to test sorting
dog.add_task(Task(description="Evening feeding", duration=10, priority=2, due_time="2026-03-31 18:00", frequency="daily"))
cat.add_task(Task(description="Play time", duration=20, priority=3, due_time="2026-03-31 12:00"))
dog.add_task(Task(description="Morning walk", duration=30, priority=1, due_time="2026-03-31 07:00", frequency="daily"))
cat.add_task(Task(description="Litter box cleaning", duration=15, priority=1, due_time="2026-03-31 08:00", frequency="weekly"))
dog.add_task(Task(description="Afternoon nap check", duration=5, priority=3, due_time="2026-03-31 14:00"))
# Conflicting tasks: vet visit overlaps with morning walk (07:00 + 30 min = 07:30)
dog.add_task(Task(description="Vet visit", duration=60, priority=1, due_time="2026-03-31 07:15"))

scheduler = Scheduler(owner)

# 1. Full schedule sorted by time
print("=" * 50)
print("  Today's Schedule for", owner.name)
print("=" * 50)
plan = scheduler.generate_plan()
print(scheduler.explain_plan(plan))

# 2. Conflict detection
print("\n" + "=" * 50)
print("  Conflict Detection")
print("=" * 50)
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"  ⚠ {warning}")
else:
    print("  No conflicts detected.")

# 3. Filter by pet
print("\n" + "=" * 50)
print("  Mochi's Tasks")
print("=" * 50)
mochi_tasks = scheduler.filter_by_pet("Mochi")
print(scheduler.explain_plan(scheduler.sort_by_time(mochi_tasks)))

print("\n" + "=" * 50)
print("  Whiskers' Tasks")
print("=" * 50)
whiskers_tasks = scheduler.filter_by_pet("Whiskers")
print(scheduler.explain_plan(scheduler.sort_by_time(whiskers_tasks)))

# 3. Recurring task demo
print("\n" + "=" * 50)
print("  Recurring Task Demo")
print("=" * 50)
walk = dog.tasks[1]  # Morning walk (daily)
print(f"Before completing: {walk.description} due {walk.due_time}")
walk.toggle_complete()
print(f"After completing:  {walk.description} due {walk.due_time} (auto-advanced to tomorrow)")

litter = cat.tasks[1]  # Litter box cleaning (weekly)
print(f"\nBefore completing: {litter.description} due {litter.due_time}")
litter.toggle_complete()
print(f"After completing:  {litter.description} due {litter.due_time} (auto-advanced by 1 week)")

# 4. Mark a non-recurring task complete
cat.tasks[0].toggle_complete()  # Complete "Play time"

print("\n" + "=" * 50)
print("  Completed Tasks")
print("=" * 50)
completed = scheduler.filter_by_status(completed=True)
print(scheduler.explain_plan(completed))

print("\n" + "=" * 50)
print("  Updated Schedule")
print("=" * 50)
updated_plan = scheduler.generate_plan()
print(scheduler.explain_plan(updated_plan))
print("=" * 50)
