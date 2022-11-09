#simple calculator project 


print('Enter "help" for commands')


def getinput():
   user_input = input('command: ')
   return user_input


def handle_input():
    while True:
        user_input = getinput()
        if(user_input.isdigit()):
            print('its digit')
            return False
        else:
            print('wrong input')

def main():
    handle_input()

main()