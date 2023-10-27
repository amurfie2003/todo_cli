import os

#display the menu options on the console
def display_main_menu():
    print("================ TODOs ===============")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")
    print("====================================")
    return 


#get user menu selection
def get_main_menu_selection():
    value = input("What would you like to do: ")
    menu_selected = int(value)

    if menu_selected == 1:
        print(f"menu: {menu_selected}")
        clear_console()
        print("1. View Tasks")
        print("=================================")
    elif menu_selected == 2:
        clear_console()
        print("2. Add Tasks")
        print("=================================")
    elif menu_selected == 3:
        clear_console()
        exit_vlaue = input("3. would you like to exit (y/n): ")
        print("=================================")
    return



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def main():
    display_main_menu()
    get_main_menu_selection()
    return

main()