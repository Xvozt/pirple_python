import os

question = input("Enter the filename: ")
filename = question + '.txt'


def note_type(name):
    if os.path.isfile('./' + name + '.txt') == True:
        return input('input A if u wanna read the file \n' +
                     'Input B if u wanna delete the file and start over \n' +
                     'Input C if u wanna append the file \n' + 
                     'Input D if u wanna replace a single line \n')
    else:
        return input('Input the text you wanna write to the file: ')


def writer():
    text = str(note_type(question))
    with open(filename, 'w') as f:
        f.write(text)


writer()
