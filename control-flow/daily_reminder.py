# daily_reminder.py

# Prompt for user input
task = input("Please enter the task description: ")
priority = input("What is the priority level of the task (high, medium, low)? ").lower()
time_bound = input("Is this task time-sensitive (yes or no)? ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Task: '{task}' is of high priority."
    case "medium":
        reminder = f"Task: '{task}' is of medium priority."
    case "low":
        reminder = f"Task: '{task}' is of low priority."
    case _:
        reminder = "Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
elif time_bound == "no":
    reminder += " You can attend to this later."

# Provide the customized reminder
print(reminder)