#Makes a personal daily reminder based on task, priority, and time-bound or not
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = "'" + task + "'"
match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", reminder, "is a", priority, "priority task that requires immediate attention today!") 
        else:
            print("Reminder:", reminder, "is a", priority, "priority task that is not urgent. Consider completing it during your break time!")
    case "medium":
        if time_bound == "yes":
            print("Reminder:", reminder, "is a", priority, "priority task that requires your attention before the end of the day!") 
        else:
            print("Reminder", reminder, "is a", priority, "priority task that is not urgent. Consider completing it sooner than later!")
    case "low":
        if time_bound == "yes":
            print("Reminder:", reminder, "is a", priority, "priority task that requires your attention") 
        else:
            print("Reminder", reminder, "is a", priority, "priority task that is not urgent. Consider completing it during your free time!")
