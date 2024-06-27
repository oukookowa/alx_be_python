#Makes a personal daily reminder based on task, priority, and time-bound or not
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a low priority task that is not urgent. Consider completing it during your break time!"
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that requires your attention before the end of the day!"
        else:
            reminder = f"'{task}' is a medium priority task that is not urgent. Consider completing it sooner than later!"
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority priority task that requires your attention" 
        else:
            reminder = f"'{task}' is a low priority task that is not urgent. Consider completing it during your free time!"
print("Reminder:", reminder)
