import datetime

# Function definitions


def reg_user():
    with open("user.txt", "r") as file:
        usernames = [line.strip().split(", ")[0] for line in file]
        if new_username in usernames:
            print("This username is already taken, please choose another one")
            return
        else:
            with open("user.txt", "a") as file:
                file.write(f"{new_username}, {new_password}\n")
                print("New user registered successfully!")


def add_task():
    with open("tasks.txt", "a") as file:
        file.write(f"{username}, {task_title}, {task_description}, {task_due_date}, {current_date}, No\n")
        return {username}, {task_title}, {task_description}, {task_due_date}, {current_date}


def view_all():
    with open("tasks.txt", "r") as file1:
        tasks = file1.readlines()

    # Initialize the variables with default values
    task_information = []
    username1 = ""
    title = ""
    description = ""
    due_date = ""
    assigned_date1 = ""
    status1 = ""

    for task in tasks:
        task_info = task.strip().split(", ")
        if len(task_info) < 6:
            print("Error: Invalid task format. Skipping this task.")
            continue

        username1 = task_info[0]
        title = task_info[1]
        description = task_info[2]
        due_date = task_info[3]
        assigned_date1 = task_info[4]
        status1 = task_info[5]

        print("Username: " + username1)
        print("Task Title: " + title)
        print("Task Description: " + description)
        print("Assigned Date: " + assigned_date1)

        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            try:
                due_date_obj = datetime.datetime.strptime(due_date, "%d %b %Y").date()
            except ValueError:
                print("Error: Due date has an invalid format. Skipping this task.")
                continue

        print("Due Date: " + str(due_date_obj))
        print("Status: " + status1)
        print()

        # Assigning valid task_info to task_information
        task_information = task_info

    return task_information, username1, title, description, due_date, assigned_date1, status1


def view_mine():
    tasks = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_information = line.strip().split(", ")
            username2 = task_information[0]
            task_title2 = task_information[1]
            task_description2 = task_information[2]
            assigned_date2 = task_information[3]
            task_due_date2 = task_information[4]
            status2 = task_information[5]

            if username2 == live_user:
                tasks.append(task_information)

    if not tasks:
        print("No tasks assigned to you.")
        return

    # Displaying tasks with corresponding numbers
    print("Tasks assigned to you:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. Task Title: {task[1]}")
        print(f"   Task Description: {task[2]}")
        print(f"   Assigned Date: {task[3]}")
        print(f"   Due Date: {task[4]}")
        print(f"   Status: {task[5]}")
        print()

    # Creating task selection menu
    while True:
        selection = input("Enter the number of the task you want to select (-1 to return to the main menu): ")
        if selection == "-1":
            return
        elif selection.isdigit():   # isdigit() is used to check if the input is a valid integer
            task_index = int(selection) - 1
            if task_index in range(len(tasks)):
                selected_task = tasks[task_index]
                print("Selected Task:")
                print("Task Title:", selected_task[1])
                print("Task Description:", selected_task[2])
                print("Assigned Date:", selected_task[3])
                print("Due Date:", selected_task[4])
                print("Status:", selected_task[5])

                if selected_task[5] == "No":
                    action = input("Select an action: \n1. Mark as complete\n2. Edit task\nEnter your choice: ")
                    if action == "1":
                        tasks[task_index][5] = "Yes"  # Mark task as complete in the tasks list
                        print("Task marked as complete.")
                        with open("tasks.txt", "w") as file:
                            for task_info in tasks:
                                file.write(", ".join(task_info) + "\n")  # Append the new info to the tasks file
                    elif action == "2":
                        if selected_task[5] == "No":
                            new_username = input("Enter a new username for the task: ")
                            new_due_date = input("Enter a new due date for the task (day-month-year): ")
                            tasks[task_index][0] = new_username  # Update username
                            tasks[task_index][4] = new_due_date  # Update due date
                            print("Task edited successfully.")
                            with open("tasks.txt", "w") as file:
                                for task_info in tasks:
                                    file.write(", ".join(task_info) + "\n")  # Append info to the tasks file
                        else:
                            print("This task has already been completed and cannot be edited.")
                    else:
                        print("Invalid input. Returning to the main menu.")
                else:
                    print("This task has already been completed and cannot be edited.")

                break
            else:
                print("Invalid task number. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


def generate_reports():
    # Task Overview
    with open("tasks.txt", "r") as file1:
        tasks = file1.readlines()

    with open("user.txt", "r") as file2:
        users = [line.strip().split(", ")[0] for line in file2]

    # Initialize dictionaries to store task info
    user_tasks = {}
    user_completed_tasks = {}
    user_uncompleted_tasks = {}
    user_overdue_tasks = {}

    for task in tasks:
        task_information = task.strip().split(", ")
        if len(task_information) < 6:
            print("Error: Invalid task format. Skipping this task.")
            continue

        username = task_information[0]
        status = task_information[5]

        # Count tasks for each user
        user_tasks[username] = user_tasks.get(username, []) + [task_information]

        if status == "Yes":
            user_completed_tasks[username] = user_completed_tasks.get(username, 0) + 1
        else:
            user_uncompleted_tasks[username] = user_uncompleted_tasks.get(username, 0) + 1

            try:
                due_date = datetime.datetime.strptime(task_information[4], "%Y-%m-%d").date()
            except ValueError:
                due_date = datetime.datetime.strptime(task_information[4], "%d %b %Y").date()

            if due_date < datetime.date.today():
                user_overdue_tasks[username] = user_overdue_tasks.get(username, 0) + 1

    # Writing task overview to a text file
    with open("task_overview.txt", "w") as file:
        file.write("Task Overview:\n")
        file.write(f"Total number of tasks: {len(tasks)}\n")
        file.write(f"Total number of completed tasks: {sum(user_completed_tasks.values())}\n")
        file.write(f"Total number of uncompleted tasks: {sum(user_uncompleted_tasks.values())}\n")
        file.write(f"Total number of overdue tasks: {sum(user_overdue_tasks.values())}\n")
        file.write("\n")

    # User Overview
    with open("user_overview.txt", "w") as file:
        file.write("User Overview:\n")
        for user in users:
            user_task_count = len(user_tasks.get(user, []))
            user_completed_count = user_completed_tasks.get(user, 0)
            user_uncompleted_count = user_uncompleted_tasks.get(user, 0)
            user_overdue_count = user_overdue_tasks.get(user, 0)

            if user_task_count > 0:
                user_task_percentage = (user_task_count / len(tasks)) * 100.0
            else:
                user_task_percentage = 0.0

            if user_completed_count > 0:
                user_completed_percentage = (user_completed_count / user_task_count) * 100.0
            else:
                user_completed_percentage = 0.0

            if user_uncompleted_count > 0:
                user_uncompleted_percentage = (user_uncompleted_count / user_task_count) * 100.0
            else:
                user_uncompleted_percentage = 0.0

            if user_overdue_count > 0:
                user_overdue_percentage = (user_overdue_count / user_task_count) * 100.0
            else:
                user_overdue_percentage = 0.0

            file.write(f"User: {user}\n")
            file.write(f"Total tasks assigned: {user_task_count}\n")
            file.write(f"Percentage of tasks assigned: {user_task_percentage:.2f}%\n")
            file.write(f"Percentage of completed tasks: {user_completed_percentage:.2f}%\n")
            file.write(f"Percentage of uncompleted tasks: {user_uncompleted_percentage:.2f}%\n")
            file.write(f"Percentage of overdue tasks: {user_overdue_percentage:.2f}%\n")
            file.write("\n")


# Making username valid
valid_username = False

# Making password valid
valid_password = False

while not valid_username or not valid_password:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    with open("user.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(", ")
            if username == stored_username:
                valid_username = True
            if password == stored_password:
                valid_password = True

                # live_user variable to account for the current user logged in (used later in the program)
                live_user = stored_username

    if not valid_username:
        print("Please enter a valid username.")
    if not valid_password:
        print("Please enter a valid password.")

print("You have successfully logged in!")

# While True statement to loop menu until the user decides to exit
while True:
    if live_user == "admin":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate reports
        ds - Display reports
        s - Statistics
        e - Exit
        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        e - Exit
        : ''').lower()

    # Making sure the new password matches the confirmed password
    # if statement checks to confirm if admin is logged in
    if menu == "r" and live_user == "admin":
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm the password: ")

        # calling reg_user function to add a new user to user.txt
        if new_password != confirm_password:
            print("Password and confirmation do not match. Registration failed.")
        else:
            reg_user()

    # Creating variables for a new task
    # Importing the current time and date to use as instructed
    # Appending a new task to tasks.txt
    elif menu == "a":
        username = input("Enter the username of the person whose task you'd like to add: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (yyyy-mm-dd): ")
        current_date = datetime.date.today()
        add_task()
        print("You have successfully added this task!")

    # Calling view_all function created in the beginning
    elif menu == "va":
        view_all()

    # Calling view_mine function created in the beginning
    elif menu == "vm":
        view_mine()

    # New "gr" option in the menu for admin use only
    elif menu == "gr" and live_user == "admin":
        generate_reports()
        print("Reports generated successfully!")

    # New "ds" option to display the contents of the reports for admin use only
    elif menu == "ds" and live_user == "admin":
        # Display contents of the text files
        with open("task_overview.txt", "r") as file1:
            print(file1.read())

        with open("user_overview.txt", "r") as file2:
            print(file2.read())

    # Creating admin menu option for statistics
    # Initialising a counter and using a for loop to iterate over each user and task
    elif menu == "s":
        with open("user.txt", "r") as file:
            i = -1
            for line in file:
                i += 1
        print(" ")
        print(f"Total number of users (excluding admin) = {i}")

        with open("tasks.txt", "r") as file2:
            i = 0
            for line in file2:
                i += 1
        print(f"Total number of tasks = {i}")

    elif menu == "e":
        print("Goodbye :)")
        break

    else:
        print("Invalid option. Please try again.")

    print()
