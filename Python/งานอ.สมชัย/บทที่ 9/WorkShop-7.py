from ModuleEmployee import *

DATAFILE = 'employee.txt'
def main():
    menu = ('='*17)+'\n| Employee Menu |\n'+('='*17)
    menu += '\n 1. Add Employee\n 2. Display Employee from File\n'
    menu += ' 3. Report Employee\n 4. Exit\nEnter Choice : '
    while True:
        choice = input(menu)
        if choice == '1': add_employee(DATAFILE)
        elif choice == '2': read_file(DATAFILE)
        elif choice == '3': report_employee(DATAFILE)
        elif choice == '4': break
        else: print('No choice, input again.')
    print('Exit Program')

if __name__ == '__main__':
    main()