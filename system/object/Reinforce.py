import random

from master  import trunc
from master  import gprint
from color   import bcolors

from .Weapon import 무기
from .Armor  import 갑옷
from .Skill  import 스킬

def 무기강화(무기):
    if 무기.강화레벨 >= 무기.최고강화레벨:
        print('이미 최고레벨 입니다.')
        return 무기
    강화확률 = 100*(무기.최고강화레벨-무기.강화레벨)/무기.최고강화레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.OKGREEN}[무기강화 성공]{bcolors.ENDC} ', end='')
        gprint(무기.이름, 무기.등급, end='')
        print(f' +{무기.강화레벨} ->', end='')
        무기.강화레벨업()
        print(f' +{무기.강화레벨}')
    else:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.FAIL}[무기강화 실패]{bcolors.ENDC} ', end='')
        gprint(무기.이름, 무기.등급, end='')
        print(f' +{무기.강화레벨} -> +{무기.강화레벨}')
    return 무기

def 장비강화(장비):
    if 장비.강화레벨 >= 장비.최고강화레벨:
        print('이미 최고레벨 입니다.')
        return 장비
    강화확률 = 100*(장비.최고강화레벨-장비.강화레벨)/장비.최고강화레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.OKGREEN}[장비강화 성공]{bcolors.ENDC} ', end='')
        gprint(장비.이름, 장비.등급, end='')
        print(f' +{장비.강화레벨} ->', end='')
        장비.강화레벨업()
        print(f' +{장비.강화레벨}')
    else:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.FAIL}[장비강화 실패]{bcolors.ENDC} ', end='')
        gprint(장비.이름, 장비.등급, end='')
        print(f' +{장비.강화레벨} -> +{장비.강화레벨}')
    return 장비

def 갑옷강화(갑옷):
    if 갑옷.강화레벨 >= 갑옷.최고강화레벨:
        print('이미 최고레벨 입니다.')
        return 갑옷
    강화확률 = 100*(갑옷.최고강화레벨-갑옷.강화레벨)/갑옷.최고강화레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.OKGREEN}[갑옷강화 성공]{bcolors.ENDC} ', end='')
        gprint(갑옷.이름, 갑옷.등급, end='')
        print(f' +{갑옷.강화레벨} ->', end='')
        갑옷.강화레벨업()
        print(f' +{갑옷.강화레벨}')
    else:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.FAIL}[갑옷강화 실패]{bcolors.ENDC} ', end='')
        gprint(갑옷.이름, 갑옷.등급, end='')
        print(f' +{갑옷.강화레벨} -> +{갑옷.강화레벨}')
    return 갑옷

def 스킬강화(스킬):
    if 스킬.레벨 >= 스킬.최고레벨:
        print('이미 최고레벨 입니다.')
        return 스킬
    강화확률 = 5 + 95*(스킬.최고레벨-스킬.레벨)/스킬.최고레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.OKGREEN}[스킬강화 성공]{bcolors.ENDC} ', end='')
        gprint(스킬.이름, 스킬.등급, end='')
        print(f' +{스킬.레벨} ->', end='')
        스킬.스킬레벨업()
        print(f' +{스킬.레벨}')
    else:
        #print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'{bcolors.FAIL}[스킬강화 실패]{bcolors.ENDC} ', end='')
        gprint(스킬.이름, 스킬.등급, end='')
        print(f' +{스킬.레벨} -> +{스킬.레벨}')
    return 스킬
