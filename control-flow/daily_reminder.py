# task_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()

# Process based on priority using match case
match priority.lower():
    case "high":
        print(f"Reminder: {task} is a HIGH priority task")
    case "medium":
        print(f"Reminder: {task} is a MEDIUM priority task.")
    case "low":
        print(f"Reminder: {task} is a LOW priority task.")
    case _:
        print(f"Reminder: {task} has an UNKNOWN priority.")

# Modify message if time-bound
if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print ("Consider completing it when you have free time")
