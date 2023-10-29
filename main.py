import utils
from task import Task
from todo_list import TodoList


print("----------Welcome------------")
user_name = input("Please enter your user name: ")
todos = TodoList(user_name)

utils.clear_console()
utils.display_main_menu()
menu_selection = utils.get_main_menu_selection()

if menu_selection == 1:
    todos.view_task()



