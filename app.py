import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

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

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task description", value="Morning walk")
with col2:
    duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.number_input("Priority (1=high)", min_value=1, max_value=5, value=1)
with col4:
    due_time = st.text_input("Due time", value="07:00")

if st.button("Add Task"):
    pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet)
    task = Task(description=task_title, duration=float(duration), priority=priority, due_time=due_time)
    pet.add_task(task)

all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table([{"pet": p.name, "task": t.description, "duration": t.duration, "priority": t.priority, "due": t.due_time, "done": t.completed} for p in st.session_state.owner.pets for t in p.tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(st.session_state.owner)
    plan = scheduler.generate_plan()
    if plan:
        st.markdown(scheduler.explain_plan(plan))
    else:
        st.info("No incomplete tasks to schedule.")
