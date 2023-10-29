import task as Task

class TodoList:
    def __init__(self, user_name):
        self.user_name = user_name
        self.list_of_tasks = []
        return

    def create_task(self):
        self.task_name = input("Give your task a name: ")
        new_task = Task(self.task_name)
        self.list_of_tasks.append(new_task)
         
        while self.task_name.lower() != 'n':
            self.task_name= input("Would you like to add another task [y/n]: ")
            if self.task_name.lower() == 'y':
                self.task_name = input("what task would you like to add: ")
                new_task = Task(self.task_name)
                self.tasks.append(new_task)
    
    def view_task(self):
        total_task = len(self.tasks)
        print(f"You currently have {total_task} tasks")
        print("=================================")

        if total_task > 0:
            for task in self.task:
                print(f"-{task.name} \n\tstatus: {'Complete' if task.status else 'Incomplete'}")
        return 
