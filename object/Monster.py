import random

from master                   import trunc
from color                    import bcolors

from .Character               import 캐릭터
from .Skill                   import 스킬
from .Weapon                  import *

class 몬스터(캐릭터):
    def __init__(self, 이름):
        super().__init__(이름)
        self.등급 = 1
        self.직업 = '일반'
        self.무기 = 무기('주황버섯의 갓')
        self.HP = 500
        self.공격력 = 40
        self.스킬리스트 = []
        self.스킬리스트.append(스킬('박치기'))
        self.경험치 = 2500
        self.코인 = 200

    def 출력(self):
        print('==============================')
        print(f'{bcolors.BOLD}{self.이름}{bcolors.ENDC}[{self.직업}] Lv.{self.레벨}')
        if self.무기 != None: self.무기.출력()
        print(f'HP         : {self.HP}')
        print(f'공격력     : {self.공격력}')
        print(f'방어력     : {self.방어력}')
        print(f'내성       : {trunc(self.내성, 2)}')
        print(f'명중       : {self.명중}')
        print(f'회피       : {trunc(self.회피, 2)}')
        print(f'치명타     : {trunc(self.치명타, 2)}')
        print(f'치명타증폭 : {trunc(self.치명타증폭, 2)}')
        print(f'최종데미지 : {int(self.공격력 + self.무기.최종증폭*self.무기.최종최소데미지)} - {int(self.공격력 + self.무기.최종증폭*self.무기.최종최대데미지)}')
        print(f'보유스킬   : {self.스킬리스트[0].이름} Lv.{self.스킬리스트[0].레벨}')
        for 스킬 in self.스킬리스트[1:]:
            print(f'             {스킬.이름} Lv.{스킬.레벨}')
        print(f'경험치     : {self.경험치}')
        print('==============================')

def 산적():
    산적 = 몬스터('산적')
    산적.무기 = 무기('무딘 칼')
    산적.레벨 = 2
    산적.HP = 750
    산적.공격력 = 65
    산적.스킬리스트 = []
    산적.스킬리스트.append(스킬('휘두르기'))
    산적.경험치 = 3000
    산적.코인 = 250
    return 산적

def 구미호():
    구미호 = 몬스터('구미호')
    구미호.무기 = 혼령의구슬()
    구미호.직업 = '보스'
    구미호.레벨 = 80
    구미호.HP = 108000
    구미호.공격력 = 900
    구미호.치명타 = 0.6
    구미호.치명타증폭 = 1.4
    구미호.회피 = 0.5
    구미호.내성 = 0.2
    구미호.스킬리스트 = []
    구미호.스킬리스트.append(스킬('매혹'))
    구미호.스킬리스트.append(스킬('요괴화'))
    구미호.경험치 = 548000
    구미호.코인 = 10800
    return 구미호
    