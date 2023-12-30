from master import trunc
from color  import bcolors

from character import 캐릭터
from skill     import 스킬
from weapon    import 무기

class 몬스터(캐릭터):
    def __init__(self, 이름):
        super().__init__(이름)
        self.직업 = ''
        self.무기 = 무기('주황버섯의 갓')
        self.HP = 500
        self.공격력 = 40
        self.스킬리스트 = []
        self.스킬리스트.append(스킬('박치기'))  # 강타
        self.경험치 = 2500

    def 출력(self):
        print('==============================')
        print(f'{bcolors.BOLD}{self.이름}{bcolors.ENDC}[{self.직업}] Lv.{self.레벨}')
        if self.무기 != None: self.무기.출력()
        print(f'HP         : {self.HP}')
        print(f'공격력     : {self.공격력}')
        print(f'방어력     : {self.방어력}')
        print(f'치명타     : {trunc(self.치명타, 2)}')
        print(f'명중       : {self.명중}')
        print(f'회피       : {trunc(self.회피, 2)}')
        print(f'최종데미지 : {int(self.공격력 + self.무기.최종증폭*self.무기.최종최소데미지)} - {int(self.공격력 + self.무기.최종증폭*self.무기.최종최대데미지)}')
        print(f'보유스킬   : {self.스킬리스트[0].이름} Lv.{self.스킬리스트[0].레벨}')
        for 스킬 in self.스킬리스트[1:]:
            print(f'             {스킬.이름} Lv.{스킬.레벨}')
        print(f'경험치     : {self.경험치}')
        print('==============================')