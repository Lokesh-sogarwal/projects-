def show_tasks(tasks):
    if not tasks:
        print("Your to-do list memo is empty.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task[0]} {'(Done)' if task[1] else ''}")

def add_task(tasks, task_name):
    tasks.append([task_name, False])
    print(f"Task '{task_name}' got added to your to-do list.")

def remove_task(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task[0]}' got removed from your to-do list.")
    else:
        print("Invalid task number!")

def mark_as_done(tasks, task_index):
    if task_index >= 1 and task_index <= len(tasks):
        tasks[task_index - 1][1] = True
        print(f"Task marked as done.")
    else:
        print("Invalid task number!")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application :)")
        print("Select one of the drop-down to continue")
        
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task_name = input("Enter the task name: ")
            add_task(tasks, task_name)
        elif choice == "3":
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to mark as done: "))
            mark_as_done(tasks, task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please retry!.")
if _name_ == "_main_":
main()