import random

from object.Town       import 마을
from object.Character  import 캐릭터

from .dual             import dual
from .create_monster   import create_monster

def hunt(내캐릭터, 상대몬스터):
    승자 = dual(내캐릭터, 상대몬스터)
    if 승자 == 내캐릭터.이름:
        내캐릭터.경험치 += 상대몬스터.경험치
        내캐릭터.코인   += int(random.uniform(0.95, 1.05)*상대몬스터.코인)
        while 내캐릭터.경험치 >= 내캐릭터.필요경험치:
            내캐릭터.경험치 -= 내캐릭터.필요경험치
            내캐릭터.필요경험치 += 1000
            내캐릭터.레벨업()

if __name__ == '__main__':
    불러온캐릭터 = 캐릭터('불러온캐릭')
    불러온캐릭터.불러오기('갓종')
    불러온캐릭터.출력()
    create_monster('주황버섯')
    for _ in range(10): hunt(불러온캐릭터, 마을.불러오기('주황버섯'))
    불러온캐릭터.출력()