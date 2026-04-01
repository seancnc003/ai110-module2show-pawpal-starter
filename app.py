import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.caption("A smart pet care planning assistant")

st.divider()

# Initialize session state
if "owner" not in st.session_state:
    st.session_state.owner = None

st.subheader("Owner Setup")
owner_name = st.text_input("Owner name", value="Jordan")
time_available = st.number_input("Time available (minutes)", min_value=1, max_value=480, value=120)

if st.button("Create Owner"):
    st.session_state.owner = Owner(name=owner_name, time_available=time_available)

if st.session_state.owner is None:
    st.info("Create an owner to get started.")
    st.stop()

st.success(f"Owner: {st.session_state.owner.name} ({st.session_state.owner.time_available} min available)")

st.divider()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    pet = Pet(name=pet_name, animal_type=species)
    st.session_state.owner.add_pet(pet)

if not st.session_state.owner.pets:
    st.info("No pets yet. Add one above.")
    st.stop()

st.write("Pets:", [f"{p.name} ({p.animal_type})" for p in st.session_state.owner.pets])

st.divider()

st.subheader("Add a Task")
pet_choices = [p.name for p in st.session_state.owner.pets]
selected_pet = st.selectbox("Assign to pet", pet_choices)

col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task description", value="Morning walk")
    due_date = st.date_input("Due date")
with col2:
    duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    due_time_input = st.time_input("Due time")

col3, col4 = st.columns(2)
with col3:
    priority = st.number_input("Priority (1=high)", min_value=1, max_value=5, value=1)
with col4:
    frequency = st.selectbox("Frequency", ["none", "daily", "weekly"])

if st.button("Add Task"):
    pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet)
    due_time_str = f"{due_date.strftime('%Y-%m-%d')} {due_time_input.strftime('%H:%M')}"
    task = Task(description=task_title, duration=float(duration), priority=priority, due_time=due_time_str, frequency=frequency)
    pet.add_task(task)

all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table([{
        "pet": p.name,
        "task": t.description,
        "duration": t.duration,
        "priority": t.priority,
        "due": t.due_time,
        "frequency": t.frequency,
        "done": t.completed
    } for p in st.session_state.owner.pets for t in p.tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Schedule")

scheduler = Scheduler(st.session_state.owner)

# Conflict detection
conflicts = scheduler.detect_conflicts()
if conflicts:
    for conflict in conflicts:
        st.warning(f"⚠️ {conflict}")

# Filter by pet
filter_option = st.selectbox("Filter by pet", ["All pets"] + pet_choices)

if st.button("Generate Schedule"):
    if filter_option == "All pets":
        plan = scheduler.generate_plan()
    else:
        pet_tasks = scheduler.filter_by_pet(filter_option)
        incomplete = [t for t in pet_tasks if not t.completed]
        plan = scheduler.sort_by_time(incomplete)

    if plan:
        st.success("Schedule generated!")
        st.table([{
            "order": i + 1,
            "task": t.description,
            "due": t.due_time,
            "duration": f"{t.duration} min",
            "priority": t.priority
        } for i, t in enumerate(plan)])
    else:
        st.info("No incomplete tasks to schedule.")
