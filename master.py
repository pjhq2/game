from color import bcolors

def trunc(number, ndigits):
    if type(number) == float:
        temp = str(number).split('.')
        return temp[0] + '.' + temp[1][:ndigits]
    elif type(number) == int:
        return str(number) + '.00'
    else:
        raise(TypeError)

def gprint(string, grade):
    if   grade <= 1: print(string)
    elif grade == 2: print(f'{bcolors.OKGREEN}{string}{bcolors.ENDC}')
    elif grade == 3: print(f'{bcolors.OKBLUE}{string}{bcolors.ENDC}')
    elif grade == 4: print(f'{bcolors.FAIL}{string}{bcolors.ENDC}')
    elif grade == 5: print(f'{bcolors.HEADER}{string}{bcolors.ENDC}')
    else:            print(f'{bcolors.WARNING}{string}{bcolors.ENDC}')
    