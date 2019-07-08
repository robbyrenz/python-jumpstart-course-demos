def main():  # defining a main method; high level code up here
    print_header()
    run_event_loop()


# main() can't be defined here as Python would not know the implementations of the functions in the main method

def print_header():
    print('-------------------------------')
    print('         JOURNAL APP')
    print('-------------------------------')


def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entries()
        elif cmd != 'x':
            print('Sorry, we don\'t understand \'{}\'.'.format(cmd))

    print('Done, goodbye.')


def list_entries():
    print('Listing...')


def add_entries():
    print('Adding...')


main()
