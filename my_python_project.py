#simple calculator project 


print('Enter "help" for commands')


def handle_input():
    user_input = input('command: ')
    while len(user_input) or user_input.isdigit() == False <= 0 :
        user_input = input('command: ')
        if(len(user_input) > 0 and user_input.isdigit()):
            break
        

def main():
    handle_input()

main()