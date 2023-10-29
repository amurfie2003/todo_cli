import os

#clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


#get generic user input
def get_user_input(prompt):
    prompt += ": "
    value = input(prompt)
    return value


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
        print("exit")
        print("=================================")

    return menu_selected