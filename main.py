import utility as utils


class Task:
    def __init__(self, name):
        self.name = name
        self.status = False
        return


class Todo:
    def __init__(self, user_name):
        self.user_name = user_name
        self.tasks = []
        return

    def add_task(self):
        self.task_name = input("what task would you like to add: ")
        new_task = Task(self.task_name)
        self.tasks.append(new_task)
         
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

   


#Testing
print("----------Welcome------------")
user_name = input("Please enter your user name: ")
todo = Todo(user_name)

utils.clear_console()
utils.display_main_menu()
menu_selection = utils.get_main_menu_selection()

if menu_selection == 1:
    todo.view_task()



