import datetime  # in order to work with dates, we have to import this module


def print_header():
    print('-----------------------------------------------')
    print('                 BIRTHDAY APP')
    print('-----------------------------------------------')
    print()


def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('Year [YYYY]: '))  # everything that comes out of an input function is a string!
    month = int(input('Month [MM]: '))  # int() so that we can convert it to a number!
    day = int(input('Day [DD]: '))

    # datetime.datetime is for working with hours, minutes & seconds
    birthday = datetime.date(year, month, day)
    # 'datetime' before the '.' is the module; 'date' after the '.' is the class name that is contained in the module
    return birthday


def compute_days_between_days(birthday_date, today_date):
    # set the year of the birthday to today's year
    this_year = datetime.date(today_date.year, birthday_date.month, birthday_date.day)
    dt = this_year - today_date  # get the difference
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year'.format(-days))
    elif days > 0:
        print('Your birthday is coming up in {} days!'.format(days))
    else:
        print('Happy birthday!!!')


def main():  # just a convention, you don't have to name it main
    print_header()  # prints the fancy header
    bday = get_birthday_from_user()  # gets the birthday of the user
    today = datetime.date.today()  # this will return today's date!
    number_of_days = compute_days_between_days(bday, today)  # gets the difference of the dates
    print_birthday_information(number_of_days)


main()  # not the best way to call the main method
