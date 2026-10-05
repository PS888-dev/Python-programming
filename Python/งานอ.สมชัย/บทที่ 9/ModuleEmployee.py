# Filename : ModuleEmployee.py


def add_employee(filename):
    print('Enter data employee.')
    emp_id = input('Input employee id : ').strip()
    emp_name = input('Input employee name : ').strip()
    emp_surname = input('Input employee surname : ').strip()
    emp_salary = input('Input employee salary : ').strip()

    with open(filename, 'a', encoding='UTF_8') as fout:
        data = f"{emp_id},{emp_name},{emp_surname},{emp_salary}\n"
        fout.write(data)
    print('Save Data Employee already.\n')


def read_file(filename):
    try:
        with open(filename, encoding='UTF_8') as fin:
            for data in fin:
                print(data, end="")
    except FileNotFoundError:
        print(f'File {filename} not found.\n')


def read_to_memory(filename):
    datas = []
    try:
        with open(filename, encoding='UTF_8') as fin:
            for data in fin:
                data = data.rstrip('\n')
                if data.strip():
                    datas.append(data.split(','))
    except FileNotFoundError:
        return datas
    return datas


def report_employee(filename):
    datas = read_to_memory(filename)
    if not datas:
        print('No employee data.\n')
        return

    mess = 'Report Employee'.center(50) + '\n'
    mess += ('-' * 50) + '\n'
    mess += '| No.|  Id  |  Name     | Surname     |   Salary  |\n'
    mess += ('-' * 50) + '\n'
    n = 1
    for data in datas:
        if len(data) < 4:
            continue
        mess += f'|{n:3} |{data[0]:5} |{data[1]:10} |{data[2]:12} |'
        mess += format(float(data[3]), ',.2f').rjust(10) + '|\n'
        n += 1
    mess += ('-' * 50) + '\n'
    print(mess)