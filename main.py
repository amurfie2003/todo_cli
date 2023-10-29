import utils
from task import Task
from todo_list import TodoList
from ui.menu import Menu


print("----------Welcome------------")
user_name = utils.get_user_input("Please enter your user name")
todos = TodoList(user_name)

utils.clear_console()
Menu.view_main_menu(user_name)



