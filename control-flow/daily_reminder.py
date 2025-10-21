task = input("Task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Time Bound (yes/no): ").lower()
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."
if time_bound == "yes":
    print(f"Reminder: {reminder} Immediate action is required!")
else:
    print(f"Note: {reminder} You can complete it when you have time.")
