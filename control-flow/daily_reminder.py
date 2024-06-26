#Makes a personal daily reminder based on task, priority, and time-bound or not
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!") 
        else:
            print(f"Note: '{task}' is a {priority} priority task that is not urgent. Consider completing it during your break time!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires your attention before the end of the day!") 
        else:
            print(f"Note: '{task}' is a {priority} priority task that is not urgent. Consider completing it sooner than later!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires your attention") 
        else:
            print(f"Note: '{task}' is a {priority} priority task that is not urgent. Consider completing it during your free time!")
