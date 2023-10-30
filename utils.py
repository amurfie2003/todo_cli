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


