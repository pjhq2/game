from master import trunc
from town   import Town
from weapon import 무기
from skill  import 스킬

from color  import bcolors

import random, os

class 캐릭터():
    def __init__(self, 이름='임시캐릭터'):
        # 스텟
        self.STR        = 5
        self.DEX        = 5
        self.INT        = 5
        self.CON        = 5
        self.LUK        = 5
        # 정보
        self.이름       = 이름
        self.레벨       = 1
        self.직업       = '초보자'
        self.공격력     = 10
        self.HP         = 2000
        self.MP         = 100
        self.명중       = 10
        self.회피       = 0.1
        self.치명타     = 0.2
        self.치명타증폭 = 1.25
        self.방어력     = 50
        self.내성       = 0.0
        self.회복       = 5
        self.속도       = 1000
        self.경험치     = 0
        self.필요경험치 = 2000
        # 장비
        self.무기       = 무기()
        # 스킬
        self.스킬리스트 = []
        self.스킬리스트.append(스킬())  # 강타

    def 최종데미지(self):
        치명타적중 = False
        최종데미지 = self.공격력 + self.무기.최종증폭*random.randint(self.무기.최종최소데미지, self.무기.최종최대데미지)
        if random.uniform(0, 1) <= self.치명타:
            치명타적중 = True
            최종데미지 *= self.치명타증폭
        return int(최종데미지), 치명타적중

    def 최종피해(self, 최종데미지, 명중):
        회피성공 = False
        if random.uniform(0, 1) <= self.회피 - 명중/100:
            회피성공 = True
            최종피해 = 0
        else:
            최종피해 = 최종데미지 - self.방어력//10
            최종피해 //= 1-self.내성
        return int(최종피해), 회피성공
    
    def 레벨업(self):
        self.레벨   += 1
        self.공격력 += 1
        self.HP     += 2
        self.방어력 += 3
        if self.직업 == '초보자':
            for i in range(5):
                if   i==0: self.STR += random.randint(1, 2)
                elif i==1: self.DEX += random.randint(1, 2)
                elif i==2: self.INT += random.randint(1, 2)
                elif i==3: self.CON += random.randint(1, 2)
                elif i==4: self.LUK += random.randint(0, 2)
        if self.직업 == '전사':
            for i in range(5):
                if   i==0: self.STR += random.randint(2, 3)
                elif i==1: self.DEX += random.randint(1, 2)
                elif i==2: self.INT += random.randint(0, 0)
                elif i==3: self.CON += random.randint(2, 3)
                elif i==4: self.LUK += random.randint(0, 1)
        elif self.직업 == '도적':
            for i in range(5):
                if   i==0: self.STR += random.randint(0, 2)
                elif i==1: self.DEX += random.randint(2, 3)
                elif i==2: self.INT += random.randint(0, 1)
                elif i==3: self.CON += random.randint(0, 1)
                elif i==4: self.LUK += random.randint(2, 3)
        self.공격력 = 10   + self.STR * 1
        self.치명타 = 0.2  + self.DEX * 0.002
        self.명중   = 10   + self.DEX * 2
        self.회복   = 5    + self.INT * 3
        self.방어력 = 50   + self.CON * 2
        self.HP     = 2000 + self.CON * 15
        self.회피   = 0.1  + self.LUK * 0.001

    def 장착_무기(self, 무기):
        for key, value in 무기.추가능력치.items():
            if   key=='STR': self.STR += value
            elif key=='DEX': self.DEX += value
            elif key=='INT': self.INT += value
            elif key=='CON': self.CON += value
            elif key=='LUK': self.LUK += value
        self.무기 = 무기

    def 해제_무기(self, 무기):
        for key, value in self.무기.추가능력치.items():
            if   key=='STR': self.STR -= value
            elif key=='DEX': self.DEX -= value
            elif key=='INT': self.INT -= value
            elif key=='CON': self.CON -= value
            elif key=='LUK': self.LUK -= value
        self.무기 = 무기()
        

    def 출력(self):
        print('==============================')
        print(f'{bcolors.BOLD}{self.이름}{bcolors.ENDC}[{self.직업}] Lv.{self.레벨}')
        self.무기.출력()
        print(f'HP         : {self.HP}')
        print(f'MP         : {self.MP}')
        print(f'STR        : {self.STR}')
        print(f'DEX        : {self.DEX}')
        print(f'INT        : {self.INT}')
        print(f'CON        : {self.CON}')
        print(f'LUK        : {self.LUK}')
        print(f'공격력     : {self.공격력}')
        print(f'방어력     : {self.방어력}')
        print(f'치명타     : {trunc(self.치명타, 2)}')
        print(f'명중       : {self.명중}')
        print(f'회피       : {trunc(self.회피, 2)}')
        print(f'최종데미지 : {int(self.공격력 + self.무기.최종증폭*self.무기.최종최소데미지)} - {int(self.공격력 + self.무기.최종증폭*self.무기.최종최대데미지)}')
        print(f'보유스킬   : {self.스킬리스트[0].이름} Lv.{self.스킬리스트[0].레벨}')
        for 스킬 in self.스킬리스트[1:]:
            print(f'             {스킬.이름} Lv.{스킬.레벨}')
        print(f'경험치     : {self.경험치} / {self.필요경험치}')
        print('==============================')

    def 저장(self):
        Town.캐릭터딕셔너리[f'{self.이름}'] = self
        if not os.path.isdir('./save'):
            os.system('mkdir ./save')
        f = open(f'./save/{self.이름}.info', 'w')
        f.write(f'이름 : {self.이름}\n')
        f.write(f'레벨 : {self.레벨}\n')
        f.write(f'STR  : {self.STR}\n')
        f.write(f'DEX  : {self.DEX}\n')
        f.write(f'INT  : {self.INT}\n')
        f.write(f'CON  : {self.CON}\n')
        f.write(f'LUK  : {self.LUK}\n')
        f.write(f'직업 : {self.직업}\n')
        f.write(f'공격력 : {self.공격력}\n')
        f.write(f'HP : {self.HP}\n')
        f.write(f'MP : {self.MP}\n')
        f.write(f'명중 : {self.명중}\n')
        f.write(f'회피 : {self.회피}\n')
        f.write(f'치명타 : {self.치명타}\n')
        f.write(f'치명타증폭 : {self.치명타증폭}\n')
        f.write(f'방어력 : {self.방어력}\n')
        f.write(f'내성 : {self.내성}\n')
        f.write(f'회복 : {self.회복}\n')
        f.write(f'속도 : {self.속도}\n')
        f.write(f'경험치 : {self.경험치}\n')
        f.write(f'필요경험치 : {self.필요경험치}\n')

        f.write(f'무기_이름 : {self.무기.이름}\n')
        f.write(f'무기_등급 : {self.무기.등급}\n')
        f.write(f'무기_등급이름 : {self.무기.등급이름}\n')
        f.write(f'무기_강화레벨 : {self.무기.강화레벨}\n')
        f.write(f'무기_최소데미지 : {self.무기.최소데미지}\n')
        f.write(f'무기_최대데미지 : {self.무기.최대데미지}\n')
        f.write(f'무기_강화최소데미지 : {self.무기.강화최소데미지}\n')
        f.write(f'무기_강화최대데미지 : {self.무기.강화최대데미지}\n')
        f.write(f'무기_강화증폭 : {self.무기.강화증폭}\n')
        f.write(f'무기_최종최소데미지 : {self.무기.최종최소데미지}\n')
        f.write(f'무기_최종최대데미지 : {self.무기.최종최대데미지}\n')
        f.write(f'무기_최종증폭 : {self.무기.최종증폭}\n')
        for key, value in self.무기.추가능력치.items():
            f.write(f'무기_추가능력치_{key} : {value}\n')
        for i, 무기스킬 in enumerate(self.무기.무기스킬리스트, 1):
            f.write(f'무기_스킬_{i}_이름 : {무기스킬.이름}\n')
            f.write(f'무기_스킬_{i}_레벨 : {무기스킬.레벨}\n')
            f.write(f'무기_스킬_{i}_등급 : {무기스킬.등급}\n')
            f.write(f'무기_스킬_{i}_데미지 : {무기스킬.데미지}\n')
            f.write(f'무기_스킬_{i}_타입 : {무기스킬.타입}\n')
            f.write(f'무기_스킬_{i}_지속시간 : {무기스킬.지속시간}\n')
            f.write(f'무기_스킬_{i}_증폭 : {무기스킬.증폭}\n')
        for i, 스킬 in enumerate(self.스킬리스트, 1):
            f.write(f'스킬_{i}_이름 : {스킬.이름}\n')
            f.write(f'스킬_{i}_레벨 : {스킬.레벨}\n')
            f.write(f'스킬_{i}_등급 : {스킬.등급}\n')
            f.write(f'스킬_{i}_데미지 : {스킬.데미지}\n')
            f.write(f'스킬_{i}_타입 : {스킬.타입}\n')
            f.write(f'스킬_{i}_지속시간 : {스킬.지속시간}\n')
            f.write(f'스킬_{i}_증폭 : {스킬.증폭}\n')
        f.close()

    def 불러오기(self, 캐릭터이름):
        if not os.path.isfile(f'./save/{캐릭터이름}.info'):
            raise(NameError)
        f = open(f'./save/{캐릭터이름}.info', 'r')
        캐릭터정보리스트 = []
        스킬딕셔너리 = {}
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            line_list = line.split(' : ')
            key_list = line_list[0].split('_')
            value = line_list[1]
            캐릭터정보리스트.append((key_list, value))
        for key_list, value in 캐릭터정보리스트:
            if len(key_list) == 1:
                if   key_list[0] == '이름': self.이름 = value
                elif key_list[0] == '레벨': self.레벨 = int(value)
                elif key_list[0] == 'STR':  self.STR  = int(value)
                elif key_list[0] == 'DEX':  self.DEX  = int(value)
                elif key_list[0] == 'INT':  self.INT  = int(value)
                elif key_list[0] == 'CON':  self.CON  = int(value)
                elif key_list[0] == 'LUK':  self.LUK  = int(value)
                elif key_list[0] == '직업': self.직업 = value
                elif key_list[0] == '공격력': self.공격력 = int(value)
                elif key_list[0] == 'HP': self.HP = int(value)
                elif key_list[0] == 'MP': self.MP = int(value)
                elif key_list[0] == '명중': self.명중 = int(value)
                elif key_list[0] == '회피': self.회피 = float(value)
                elif key_list[0] == '치명타': self.치명타 = float(value)
                elif key_list[0] == '치명타증폭': self.치명타증폭 = float(value)
                elif key_list[0] == '방어력': self.방어력 = int(value)
                elif key_list[0] == '내성': self.내성 = float(value)
                elif key_list[0] == '회복': self.회복 = int(value)
                elif key_list[0] == '속도': self.속도 = int(value)
                elif key_list[0] == '경험치': self.경험치 = int(value)
                elif key_list[0] == '필요경험치': self.필요경험치 = int(value)
            elif len(key_list) >= 2:
                if key_list[0] == '무기':
                    if   key_list[1] == '이름': self.무기.이름 = value
                    elif key_list[1] == '등급': self.무기.등급 = int(value)
                    elif key_list[1] == '등급이름': self.무기.등급이름 = value
                    elif key_list[1] == '강화레벨': self.무기.강화레벨 = int(value)
                    elif key_list[1] == '최소데미지': self.무기.최소데미지 = int(value)
                    elif key_list[1] == '최대데미지': self.무기.최대데미지 = int(value)
                    elif key_list[1] == '강화최소데미지': self.무기.강화최소데미지 = int(value)
                    elif key_list[1] == '강화최대데미지': self.무기.강화최대데미지 = int(value)
                    elif key_list[1] == '강화증폭': self.무기.강화증폭 = float(value)
                    elif key_list[1] == '최종최소데미지': self.무기.최종최소데미지 = int(value)
                    elif key_list[1] == '최종최대데미지': self.무기.최종최대데미지 = int(value)
                    elif key_list[1] == '최종증폭': self.무기.최종증폭 = float(value)
                    elif key_list[1] == '추가능력치':
                        if   key_list[2] == 'STR': self.무기.추가능력치['STR'] = int(value)
                        elif key_list[2] == 'DEX': self.무기.추가능력치['DEX'] = int(value)
                        elif key_list[2] == 'INT': self.무기.추가능력치['INT'] = int(value)
                        elif key_list[2] == 'CON': self.무기.추가능력치['CON'] = int(value)
                        elif key_list[2] == 'LUK': self.무기.추가능력치['LUK'] = int(value)
                elif key_list[0] == '스킬':
                    if key_list[1] not in 스킬딕셔너리:
                        스킬딕셔너리[key_list[1]] = {key_list[2]: value}
                    else:
                        스킬딕셔너리[key_list[1]][key_list[2]] = value

        for key1 in 스킬딕셔너리.keys():
            임시스킬 = 스킬('임시스킬')
            for key2, value in 스킬딕셔너리[key1].items():
                if key2 == '이름' and value == '강타': break

                if   key2 == '이름': 임시스킬.이름 = value
                elif key2 == '레벨': 임시스킬.레벨 = int(value)
                elif key2 == '등급': 임시스킬.등급 = int(value)
                elif key2 == '데미지': 임시스킬.데미지 = int(value)
                elif key2 == '타입': 임시스킬.타입 = value
                elif key2 == '지속시간': 임시스킬.지속시간 = int(value)
                elif key2 == '증폭': 임시스킬.증폭 = float(value)
            if 임시스킬.이름 != '임시스킬':
                self.스킬리스트.append(임시스킬)
        f.close()
        Town.캐릭터딕셔너리[f'{self.이름}'] = self
        return self
        