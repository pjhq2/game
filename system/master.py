import unicodedata

from .color import bcolors

def fill_str_with_space(input_s="", max_size=60, fill_char=" "):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)

def calc_str_length(input_s=''):
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return l

def trunc(number, ndigits):
    if type(number) == float:
        temp = str(number).split('.')
        return temp[0] + '.' + temp[1][:ndigits]
    elif type(number) == int:
        return str(number) + '.00'
    else:
        raise(TypeError)

def gprint(string, grade, end='\n'):
    if   grade <= 1: print(string, end=end)
    elif grade == 2: print(f'{bcolors.OKGREEN}{string}{bcolors.ENDC}', end=end)
    elif grade == 3: print(f'{bcolors.OKBLUE}{string}{bcolors.ENDC}', end=end)
    elif grade == 4: print(f'{bcolors.FAIL}{string}{bcolors.ENDC}', end=end)
    elif grade == 5: print(f'{bcolors.HEADER}{string}{bcolors.ENDC}', end=end)
    else:            print(f'{bcolors.WARNING}{string}{bcolors.ENDC}', end=end)
