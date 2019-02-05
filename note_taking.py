import os


def main():
    question = input("Enter the filename: ")
    filename = question + '.txt'
    if os.path.isfile('./' + filename) == True:
        a = input('Type A if u wanna read the file \n' +
                  'Type B if u wanna delete the file and start over \n' +
                  'Type C if u wanna append the file \n' + 
                  'Type D if u wanna replace a single line \n')
        if a.upper() == 'A': 
            reader(filename)
        elif a.upper() == 'B':
            deleter(filename)
            main()
        elif a.upper() == 'C':
            appender(filename) 
        elif a.upper() == 'D':
            replacer(filename)
        else:
            print('No such option')
    else:
        writer(filename)


def writer(name):
    text = input('Input the text you wanna write to the file: ')
    with open(name, 'w') as f:
        f.write(text)


def reader(name):
    with open(name, 'r') as f:
        print(f.read())


def deleter(name):
    f = open(name, 'w')
    f.close()


def appender(name):
    text = input('Input the text you wanna add to the file: ')
    with open(name, 'a') as f:
        f.write('\n'+text)
    print('Your text: ' + '"' + text + '"' + ' added')

    
def replacer(name):
    try:
        replacing_line = int(input('Enter the line number you wanna replace: '))
    except ValueError:
        print('Line number must be int')
    else:
        text = input('Enter the text: ')
        with open(name, 'r+') as f:
            line_list = f.readlines()
            if replacing_line > len(line_list):
                raise IndexError('You are trying replace line that does not exist in file')
            else: 
                line_list[replacing_line-1] = text + '\n'
        with open(name, 'w') as f:    
            for line in line_list:
                    f.write(line)
        print('Line ', replacing_line, ' was replaced')


main()
        