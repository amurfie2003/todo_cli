import utils
#

class Menu:
    @staticmethod
    def view_main_menu(user_name=""):
        print(f"===============* Welcome {user_name} *===============")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        print("=======================================================")
        return 
    
    #display the selected menu
    @staticmethod
    def main_menu_option(option, todos):
        if option == 1:
            utils.clear_console()
            print("1. View Tasks")
            print("=================================")
            todos.view_task()
        elif option == 2:
            utils.clear_console()
            print("2. Add Task")
            print("=================================")
            todos.create_task()
            utils.clear_console()
            todos.view_task()
        return 