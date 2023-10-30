import pickle
from task import Task

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
                self.list_of_tasks.append(new_task)
        
        self.task_name= input("Would you like to save your list of task [y/n]: ")
        if self.task_name.lower() == 'y':
            self.save_todos()
        
        return
    
    def view_task(self):
        #if file does not exist
        try:
            self.load_todos()
        except FileNotFoundError:
            total_task = 0
        

        total_task = len(self.list_of_tasks)
        print(f"You currently have {total_task} tasks")
        print("=================================")

        if total_task > 0:
            for task in self.list_of_tasks:
                print(f"-{task.name} \n\tstatus: {'Complete' if task.status else 'Incomplete'}")
        return 
    
    #save object to file(serialize)
    def save_todos(self):
        data = self.list_of_tasks
        with open('my_todos', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)
        return
    
    
    #load object from file(deserialize)
    def load_todos(self):
        with open('my_todos', 'rb') as pickle_file:
            loaded_data = pickle.load(pickle_file)
            for data in loaded_data:
                self.list_of_tasks.append(data)
        return



