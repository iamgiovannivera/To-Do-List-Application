# 1. To Do List Application:
    
    
# class Task:
#     def __init__(self, title):
#         self.title = title
#         self.status = "Incomplete"

#     def mark_complete(self):
#         self.status = "Complete"

#     def __str__(self):
#         return f"{self.title} - {self.status}"

# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, title):
#         new_task = Task(title)
#         self.tasks.append(new_task)
#         print(f"Task '{title}' has been added.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks in the to-do list.")
#         else:
#             for idx, task in enumerate(self.tasks, 1):
#                 print(f"{idx}. {task}")

#     def mark_task_complete(self, task_number):
#         try:
#             self.tasks[task_number - 1].mark_complete()
#             print(f"Task {task_number} marked as complete.")
#         except IndexError:
#             print("Invalid task number. Please try again.")

#     def delete_task(self, task_number):
#         try:
#             task = self.tasks.pop(task_number - 1)
#             print(f"Task '{task.title}' has been deleted.")
#         except IndexError:
#             print("Invalid task number. Please try again.")

# def display_menu():
#     print("\nWelcome to the To-Do List App!")
#     print("Menu:")
#     print("1. Add a task")
#     print("2. View tasks")
#     print("3. Mark a task as complete")
#     print("4. Delete a task")
#     print("5. Quit")

# def main():
#     to_do_list = ToDoList()
    
#     while True:
#         display_menu()
#         try:
#             choice = int(input("Select an option (1-5): "))
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 5.")
#             continue

#         if choice == 1:
#             title = input("Enter the task title: ")
#             to_do_list.add_task(title)
#         elif choice == 2:
#             to_do_list.view_tasks()
#         elif choice == 3:
#             try:
#                 task_number = int(input("Enter the task number to mark as complete: "))
#                 to_do_list.mark_task_complete(task_number)
#             except ValueError:
#                 print("Invalid input. Please enter a valid task number.")
#         elif choice == 4:
#             try:
#                 task_number = int(input("Enter the task number to delete: "))
#                 to_do_list.delete_task(task_number)
#             except ValueError:
#                 print("Invalid input. Please enter a valid task number.")
#         elif choice == 5:
#             print("Thank you for using the To-Do List App! Goodbye!")
#             break
#         else:
#             print("Invalid option. Please select a number between 1 and 5.")

# if __name__ == "__main__":
#     main()