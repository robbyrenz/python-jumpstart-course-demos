def main():  # defining a main method; high level code up here
    print_header()
    run_event_loop()


# main() can't be defined here as Python would not know the definition of the functions in the main method

def print_header():
    print('-------------------------------')
    print('         JOURNAL APP')
    print('-------------------------------')


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = None  # just initialize cmd to nothing just to get the while loop to work!

    journal_data = []  # initializes an empty list
    # you can also make a list with the list() function

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd == '':  # if the user doesn't enter anything
            # print('Please don\'t enter a newline character!')
            print('Please enter something at least!')
        elif cmd != 'x':
            print('Sorry, we don\'t understand \'{}\'.'.format(cmd))

    print('Done, goodbye.')


# the below block of code is my very own twist to this app
# def list_entries(data):
#     # print(data)
#     if len(data) == 0:  # if the length of the list is 0...
#         print('You have no saved messages!')
#     else:
#         i = 1
#         for message in data:
#             print(f'{i}. {message}')
#             # OR: print(str(i) + '. ' + message)
#             i = i + 1


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)


main()  # invoke the main method so that at least something happens!
