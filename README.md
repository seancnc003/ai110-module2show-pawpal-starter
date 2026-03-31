# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Smarter Scheduling

The Scheduler class includes the following algorithmic features:

- **Sort by time**: Tasks are sorted by due time using Python's `sorted()` with a lambda key, ensuring the schedule follows chronological order.
- **Filter by status**: Completed tasks are filtered out of the daily plan so only pending tasks appear.
- **Filter by pet**: Tasks can be viewed per pet, allowing owners to see what each pet needs individually.
- **Recurring tasks**: Tasks with a "daily" or "weekly" frequency auto-advance their due date when completed using `timedelta`, staying in the schedule indefinitely.
- **Conflict detection**: The scheduler checks for overlapping task durations (not just exact time matches) and returns warning messages for any conflicts found.

## Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The tests cover 8 behaviors across happy paths and edge cases:

- Toggle task completion
- Adding tasks increases pet's task count
- Sorting correctness (tasks added out of order return in chronological order)
- Recurring daily tasks (due date advances by 1 day, stays incomplete)
- Conflict detection with overlapping durations
- Generating a plan with a pet that has no tasks
- Filtering tasks by pet name
- Exact same time conflict detection

**Confidence Level: 4/5** -- core scheduling logic is well-tested, but edge cases like invalid time formats or removing pets with active tasks are not yet covered.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
