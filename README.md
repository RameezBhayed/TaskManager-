# TaskManager-
Description:
The Python Task Manager is a command-line application that allows users to register, add, view, edit, and generate reports for tasks. It is designed to efficiently manage tasks and user accounts. The program is equipped with user authentication, making it secure for multiple users, with an additional "admin" role for administrative functions.

Key Features:

User Registration: Users can register by providing a unique username and password. The system ensures that usernames are unique.

Task Addition: Users can add tasks, specifying the username of the task assignee, task title, description, due date, and current date. Tasks are stored in a file.

View All Tasks: Users can view all tasks, displaying task details such as username, task title, description, assigned date, due date, and status.

View My Tasks: Users can view their assigned tasks, mark tasks as complete, and edit tasks (for uncompleted tasks).

Generate Reports (Admin Only): The admin user can generate reports summarizing task statistics. These reports include the total number of tasks, completed tasks, uncompleted tasks, and overdue tasks.

Display Reports (Admin Only): Admin users can view the contents of the generated reports, providing valuable insights into task management.

User and Task Statistics (Admin Only): Admins can access statistics, such as the total number of registered users (excluding the admin) and the total number of tasks in the system.

Usage:

Users need to log in with a valid username and password.
The system ensures password validation and prevents duplicate usernames.
The main menu offers options based on user roles (admin or regular user).
Regular users can register, add tasks, view tasks, or exit.
Admins have additional options to generate reports, display reports, view statistics, and exit.
Conclusion:
The Python Task Manager is a versatile tool for organizing tasks and managing user accounts. It offers a range of features to facilitate task tracking, and the admin-specific functions provide valuable insights into task statistics. This project demonstrates proficiency in Python and file handling, making it a valuable addition to any portfolio.
