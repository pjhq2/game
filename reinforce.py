from master import trunc

from weapon import 무기
from skill  import 스킬

import random

def 무기강화(무기):
    if 무기.강화레벨 >= 무기.최고강화레벨:
        print('이미 최고레벨 입니다.')
        return 무기
    강화확률 = 100*(무기.최고강화레벨-무기.강화레벨)/무기.최고강화레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'[무기강화 성공] {무기.이름} +{무기.강화레벨} -> ', end='')
        무기.강화레벨업()
        print(f'+{무기.강화레벨}')
    else:
        print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'[무기강화 실패] {무기.이름} +{무기.강화레벨} -> +{무기.강화레벨}')
    return 무기

def 스킬강화(스킬):
    if 스킬.레벨 >= 스킬.최고레벨:
        print('이미 최대레벨 입니다.')
        return 스킬
    강화확률 = 5 + 95*(스킬.최고레벨-스킬.레벨)/스킬.최고레벨
    강화성공 = False
    if random.randint(1, 100) <= 강화확률: 강화성공 = True
    if 강화성공:
        print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'[스킬강화 성공] {스킬.이름} +{스킬.레벨} -> ', end='')
        스킬.스킬레벨업()
        print(f'+{스킬.레벨}')
    else:
        print(f'{trunc(강화확률, 2)}% ', end='')
        print(f'[스킬강화 실패] {스킬.이름} +{스킬.레벨} -> +{스킬.레벨}')
    return 스킬