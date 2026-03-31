# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

my initial design has 4 main classes. the owner is the main class and the pet, task, 
and scheduler classes are part of the owner. 

the owner has a name and a list of pets and tasks. we can add pets or tasks to them.
the owner has a class pet. the class pet has a name and animal type.
the owner also has a class task. the task has a type of class, and a duration, priority,
    and which pet the task is for.
the owner also uses a class scheduler to generate tasks and explain them.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

after consulting with the AI, the design did change during the implementaion. 

some changes we did was editing the owner class. we added a way to remove pets
and a time available field to help the scheduler generate tasks based on the 
owner's time. it did suggest other changes and and potential logic bottlenecks
but we both decided that it was better to note them and implement them later.

the changes to the owner was necessary because I thought they were critical
functionality especially removing pets and how much time a user has. they had
to be addressed right away.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

for my algorithm, the main consideration or filtering I did for was based on time due.
I thought that it mattered most because I thought that it would be better to complete
a lot of tasks instead of a few high priority tasks. there's also a chance that high
priority tasks get knocked out in a time due schedule. quantity was prioritized over
quality, althogh a chance for quality to be knocked out is also possible.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

my scheduler uses an algorithm with a bad time complexity. it sacrifices readability
and performance for functionality. it detects conflicts by the full amount of time 
a task is being done instead of just the times they start.

this tradeoff is reasonable for this scenario because it reflects real world scenarios.
if a task starts at 7:00 am and is 30 minutes and another task starts at 7:15 am and is
only 15 minutes, they should be conflicting since you can't do both at 7:15 am although
a more simpler algorithm based on exact start times would say that they aren't conflicting.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
