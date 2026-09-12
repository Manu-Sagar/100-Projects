from task import PersonalTask, WorkTask

class TaskManager:

    def __init__(self):
        self.tasks=[]
        self.next_id=1

    def add_task(self, title, task_type):
        if task_type.lower()=="personal":
            task=PersonalTask(self.next_id, title)
        elif task_type.lower()=="work":
            task=WorkTask(self.next_id, title)
        else:
            print("Invalid task type.")
            return

        self.tasks.append(task)
        self.next_id+=1
        print("Task added successfully.")

    def view_tasks(self):
        if len(self.tasks)==0:
            print("No tasks found.")
            return
        print("\n===== YOUR TASKS =====")

        for task in self.tasks:
            task.display()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                task.complete()
                print("Task completed successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def run(self):
        while True:
            print("\n===== TASK MANAGER =====")
            print("1. Add Personal Task")
            print("2. Add Work Task")
            print("3. View Tasks")
            print("4. Complete Task")
            print("5. Delete Task")
            print("6. Exit")

            choice=input("Enter your choice: ")

            if choice=="1":
                title = input("Enter personal task: ")
                if title.strip()=="":
                    print("Task title cannot be empty.")
                else:
                    self.add_task(title, "personal")
            elif choice=="2":
                title = input("Enter work task: ")
                if title.strip()=="":
                    print("Task title cannot be empty.")
                else:
                    self.add_task(title, "work")
            elif choice=="3":
                self.view_tasks()
            elif choice=="4":
                try:
                    task_id = int(input("Enter task ID: "))
                    self.complete_task(task_id)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice=="5":
                try:
                    task_id = int(input("Enter task ID: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "6":
                print("Thank you for using Task Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

manager = TaskManager()
manager.run()