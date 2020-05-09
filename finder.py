with open(r'progress\finder\conf', 'r', encoding='utf-8') as data:
    result = {}
    for current_line in data:
        if (current_line[0] != '#'
            and current_line[0] != ';'
                and current_line[0] != '\n'):
            if '\n' in current_line:
                current_line = current_line[:-1]
            if '#' in current_line:
                index = current_line.index('#')
                current_line = current_line[:index]

            current_line = current_line.split(' ', 1)

            try:
                result[current_line[0]] = current_line[1]
            except IndexError:
                result[current_line[0]] = "no value"


def finder():
    print("**********\n* FINDER *")
    param = input("Get param: ")
    try:
        print(result[param], end="")
        print('\n')
    except KeyError:
        print("\nError: Param not found!")
        print("Available params: ")
        note()


def note():
    for key in result:
        print(key, end='; ')
    print('\n')


close = False
while(close == False):
    attempt = 0  # for (Y/N)
    finder()
    while (attempt < 3):
        answer = input("Restart FINDER? (Y/N): ")
        if (answer != 'Y' and answer != 'N' and answer != 'y' and answer != 'n'):
            attempt += 1
            print("\nError: Incorrect answer! ", attempt, "/ 3")
            if attempt >= 3:
                print("\nError: Attempts are over")
                print("Closing FINDER...")
                close = True
            continue
        elif (answer == 'Y' or answer == 'y'):
            print("Restart FINDER...\n")
            break
        elif (answer == 'N' or answer == 'n'):
            print("Closing FINDER...")
            close = True
            break
