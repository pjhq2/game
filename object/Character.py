import os
import random

from master       import trunc
from color        import bcolors

from .Town        import 마을
from .Weapon      import 무기
from .Armor       import 갑옷
from .Skill       import 스킬
from .Inventory   import 인벤토리
from .Consumption import 소비

class 캐릭터():
    def __init__(self, 이름='임시캐릭터'):
        # 스텟
        self.STR            = 5
        self.DEX            = 5
        self.INT            = 5
        self.CON            = 5
        self.LUK            = 5
        self.추가STR        = 0
        self.추가DEX        = 0
        self.추가INT        = 0
        self.추가CON        = 0
        self.추가LUK        = 0
        self.최종STR        = self.STR + self.추가STR
        self.최종DEX        = self.DEX + self.추가DEX
        self.최종INT        = self.INT + self.추가INT
        self.최종CON        = self.CON + self.추가CON
        self.최종LUK        = self.LUK + self.추가LUK
        # 정보
        self.이름           = 이름
        self.레벨           = 1
        self.직업           = '초보자'
        self.공격력         = 100
        self.HP             = 2000
        self.MP             = 100
        self.명중           = 10
        self.회피           = 0.1
        self.치명타         = 0.2
        self.치명타증폭     = 1.25
        self.방어력         = 50
        self.내성           = 0.0
        self.회복           = 5
        self.속도           = 1000
        self.추가공격력     = 0
        self.추가HP         = 0
        self.추가MP         = 0
        self.추가명중       = 0
        self.추가회피       = 0.0
        self.추가치명타     = 0.0
        self.추가치명타증폭 = 0.0
        self.추가방어력     = 0
        self.추가내성       = 0.0
        self.추가회복       = 0
        self.추가속도       = 0
        self.최종공격력     = 100
        self.최종HP         = 2000
        self.최종MP         = 100
        self.최종명중       = 10
        self.최종회피       = 0.1
        self.최종치명타     = 0.2
        self.최종치명타증폭 = 1.25
        self.최종방어력     = 50
        self.최종내성       = 0.0
        self.최종회복       = 5
        self.최종속도       = 1000
        self.경험치         = 0
        self.필요경험치     = 2000
        self.코인           = 0
        self.인벤토리       = 인벤토리(self.이름)
        # 장비
        self.무기           = 무기()
        self.모자           = None
        self.갑옷           = None
        self.장갑           = None
        self.신발           = None
        self.코어           = None
        # 스킬
        self.스킬리스트     = []

    def 처음생성(self):
        self.스킬리스트.append(스킬())  # 강타

    def 능력치세팅(self):
        # 기본능력치
        self.공격력     = 100  + self.STR * 1
        self.치명타     = 0.2  + self.DEX * 0.002
        self.명중       = 10   + self.DEX * 2
        self.회복       = 5    + self.INT * 3
        self.방어력     = 50   + self.CON * 2
        self.HP         = 2000 + self.CON * 15
        self.회피       = 0.1  + self.LUK * 0.001
        self.치명타증폭 = 1.25 + self.LUK * 0.01
        # 추가능력치
        self.추가STR        = 0
        self.추가DEX        = 0
        self.추가INT        = 0
        self.추가CON        = 0
        self.추가LUK        = 0
        self.추가공격력     = 0
        self.추가HP         = 0
        self.추가MP         = 0
        self.추가명중       = 0
        self.추가회피       = 0.0
        self.추가치명타     = 0.0
        self.추가치명타증폭 = 0.0
        self.추가방어력     = 0
        self.추가내성       = 0.0
        self.추가회복       = 0
        self.추가속도       = 0
        if self.무기:
            for key, value in self.무기.추가능력치.items():
                if   key == 'STR': self.추가STR += value
                elif key == 'DEX': self.추가DEX += value
                elif key == 'INT': self.추가INT += value
                elif key == 'CON': self.추가CON += value
                elif key == 'LUK': self.추가LUK += value
        if self.갑옷:
            self.갑옷.출력()
            self.추가방어력 += self.갑옷.최종방어력
            self.추가HP     += self.갑옷.최종HP
            self.추가내성   += self.갑옷.최종내성
            self.추가명중   += self.갑옷.최종명중
            self.추가회피   += self.갑옷.최종회피
            for key, value in self.갑옷.추가능력치.items():
                if   key == 'STR': self.추가STR += value
                elif key == 'DEX': self.추가DEX += value
                elif key == 'INT': self.추가INT += value
                elif key == 'CON': self.추가CON += value
                elif key == 'LUK': self.추가LUK += value
        self.추가공격력     += self.추가STR * 1
        self.추가치명타     += self.추가DEX * 0.002
        self.추가명중       += self.추가DEX * 2
        self.추가회복       += self.추가INT * 3
        self.추가방어력     += self.추가CON * 2
        self.추가HP         += self.추가CON * 15
        self.추가회피       += self.추가LUK * 0.001
        self.추가치명타증폭 += self.추가LUK * 0.01
        # 최종능력치
        self.최종STR        = self.STR        + self.추가STR
        self.최종DEX        = self.DEX        + self.추가DEX
        self.최종INT        = self.INT        + self.추가INT
        self.최종CON        = self.CON        + self.추가CON
        self.최종LUK        = self.LUK        + self.추가LUK
        self.최종공격력     = self.공격력     + self.추가공격력
        self.최종치명타     = self.치명타     + self.추가치명타
        self.최종명중       = self.명중       + self.추가명중
        self.최종회복       = self.회복       + self.추가회복
        self.최종방어력     = self.방어력     + self.추가방어력
        self.최종HP         = self.HP         + self.추가HP
        self.최종회피       = self.회피       + self.추가회피
        self.최종치명타증폭 = self.치명타증폭 + self.추가치명타증폭

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
            if random.randrange(1, 100) <= 90:
                회피성공 = True
                최종피해 = 0
                return int(최종피해), 회피성공
        최종피해 = 최종데미지 - self.방어력//10
        최종피해 /= 1-self.내성
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
        elif self.직업 == '전사':
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
        self.능력치세팅()
        self.저장()

    def 장착_장비(self, 인덱스):
        if type(self.인벤토리.목록[인덱스]) == 무기:
            for key, value in self.무기.추가능력치.items():
                if   key=='STR': self.추가STR -= value
                elif key=='DEX': self.추가DEX -= value
                elif key=='INT': self.추가INT -= value
                elif key=='CON': self.추가CON -= value
                elif key=='LUK': self.추가LUK -= value
            for key, value in self.인벤토리.목록[인덱스].추가능력치.items():
                if   key=='STR': self.추가STR += value
                elif key=='DEX': self.추가DEX += value
                elif key=='INT': self.추가INT += value
                elif key=='CON': self.추가CON += value
                elif key=='LUK': self.추가LUK += value
            임시무기 = self.무기
            self.무기 = self.인벤토리.목록[인덱스]
            if 임시무기.이름 != '주먹': self.인벤토리.추가_인덱스(임시무기, 인덱스)
            else:                       self.인벤토리.목록[인덱스] = None
            self.능력치세팅()
            #self.최종STR = self.STR + self.추가STR
            #self.최종DEX = self.DEX + self.추가DEX
            #self.최종INT = self.INT + self.추가INT
            #self.최종CON = self.CON + self.추가CON
            #self.최종LUK = self.LUK + self.추가LUK
            self.저장()
        elif type(self.인벤토리.목록[인덱스]) == 갑옷:
            if self.갑옷 != None:
                for key, value in self.갑옷.추가능력치.items():
                    if   key=='STR': self.추가STR -= value
                    elif key=='DEX': self.추가DEX -= value
                    elif key=='INT': self.추가INT -= value
                    elif key=='CON': self.추가CON -= value
                    elif key=='LUK': self.추가LUK -= value
                for key, value in self.인벤토리.목록[인덱스].추가능력치.items():
                    if   key=='STR': self.추가STR += value
                    elif key=='DEX': self.추가DEX += value
                    elif key=='INT': self.추가INT += value
                    elif key=='CON': self.추가CON += value
                    elif key=='LUK': self.추가LUK += value
                임시갑옷 = self.갑옷
                self.갑옷 = self.인벤토리.목록[인덱스]
                self.인벤토리.추가_인덱스(임시갑옷, 인덱스)
            else:
                for key, value in self.인벤토리.목록[인덱스].추가능력치.items():
                    if   key=='STR': self.추가STR += value
                    elif key=='DEX': self.추가DEX += value
                    elif key=='INT': self.추가INT += value
                    elif key=='CON': self.추가CON += value
                    elif key=='LUK': self.추가LUK += value
                self.갑옷 = self.인벤토리.목록[인덱스]
                self.인벤토리.목록[인덱스] = None
            self.능력치세팅()
            #self.최종STR = self.STR + self.추가STR
            #self.최종DEX = self.DEX + self.추가DEX
            #self.최종INT = self.INT + self.추가INT
            #self.최종CON = self.CON + self.추가CON
            #self.최종LUK = self.LUK + self.추가LUK
            self.저장()
            

    def 해제_무기(self):
        if self.무기.이름 == '주먹': return
        for key, value in self.무기.추가능력치.items():
            if   key=='STR': self.추가STR -= value
            elif key=='DEX': self.추가DEX -= value
            elif key=='INT': self.추가INT -= value
            elif key=='CON': self.추가CON -= value
            elif key=='LUK': self.추가LUK -= value
        self.인벤토리.추가(self.무기)
        self.무기 = 무기()
        self.최종STR = self.STR + self.추가STR
        self.최종DEX = self.DEX + self.추가DEX
        self.최종INT = self.INT + self.추가INT
        self.최종CON = self.CON + self.추가CON
        self.최종LUK = self.LUK + self.추가LUK
        self.저장()

    def 출력(self):
        print('==============================')
        print(f'{bcolors.BOLD}{self.이름}{bcolors.ENDC}[{self.직업}] Lv.{self.레벨}')
        self.무기.출력()
        if self.갑옷: self.갑옷.출력()
        print(f' HP         : {self.HP}(+{self.추가HP})')
        print(f' MP         : {self.MP}(+{self.추가MP})')
        print(f' STR        : {self.STR}(+{self.추가STR})')
        print(f' DEX        : {self.DEX}(+{self.추가DEX})')
        print(f' INT        : {self.INT}(+{self.추가INT})')
        print(f' CON        : {self.CON}(+{self.추가CON})')
        print(f' LUK        : {self.LUK}(+{self.추가LUK})')
        print(f' 공격력     : {self.공격력}(+{self.추가공격력})')
        print(f' 방어력     : {self.방어력}(+{self.추가방어력})')
        print(f' 치명타     : {trunc(self.치명타, 2)}(+{trunc(self.추가치명타, 2)})')
        print(f' 치명타증폭 : {trunc(self.치명타증폭, 2)}(+{trunc(self.추가치명타증폭, 2)})')
        print(f' 명중       : {self.명중}(+{self.추가명중})')
        print(f' 회피       : {trunc(self.회피, 2)}(+{trunc(self.추가회피, 2)})')
        print(f' 최종데미지 : {int(self.최종공격력 + self.무기.최종증폭*self.무기.최종최소데미지)} - {int(self.최종공격력 + self.무기.최종증폭*self.무기.최종최대데미지)}')
        print(f' 보유스킬   : {self.스킬리스트[0].이름} Lv.{self.스킬리스트[0].레벨}')
        for 스킬 in self.스킬리스트[1:]:
            print(f'              {스킬.이름} Lv.{스킬.레벨}')
        print(f' 경험치     : {self.경험치} / {self.필요경험치}')
        print(f' 코인       : {self.코인}')
        print('==============================')

    def 저장(self):
        마을.저장(self)
        if not os.path.isdir('./save'):
            os.mkdir('./save')
        f = open(f'./save/{self.이름}.info', 'w')
        f.write(f'이름 : {self.이름}\n')
        f.write(f'레벨 : {self.레벨}\n')
        f.write(f'직업 : {self.직업}\n')
        f.write(f'STR : {self.STR}\n')
        f.write(f'DEX : {self.DEX}\n')
        f.write(f'INT : {self.INT}\n')
        f.write(f'CON : {self.CON}\n')
        f.write(f'LUK : {self.LUK}\n')
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
        f.write(f'추가STR : {self.추가STR}\n')
        f.write(f'추가DEX : {self.추가DEX}\n')
        f.write(f'추가INT : {self.추가INT}\n')
        f.write(f'추가CON : {self.추가CON}\n')
        f.write(f'추가LUK : {self.추가LUK}\n')
        f.write(f'추가공격력 : {self.추가공격력}\n')
        f.write(f'추가HP : {self.추가HP}\n')
        f.write(f'추가MP : {self.추가MP}\n')
        f.write(f'추가명중 : {self.추가명중}\n')
        f.write(f'추가회피 : {self.추가회피}\n')
        f.write(f'추가치명타 : {self.추가치명타}\n')
        f.write(f'추가치명타증폭 : {self.추가치명타증폭}\n')
        f.write(f'추가방어력 : {self.추가방어력}\n')
        f.write(f'추가내성 : {self.추가내성}\n')
        f.write(f'추가회복 : {self.추가회복}\n')
        f.write(f'추가속도 : {self.추가속도}\n')
        f.write(f'최종STR : {self.최종STR}\n')
        f.write(f'최종DEX : {self.최종DEX}\n')
        f.write(f'최종INT : {self.최종INT}\n')
        f.write(f'최종CON : {self.최종CON}\n')
        f.write(f'최종LUK : {self.최종LUK}\n')
        f.write(f'최종공격력 : {self.최종공격력}\n')
        f.write(f'최종HP : {self.최종HP}\n')
        f.write(f'최종MP : {self.최종MP}\n')
        f.write(f'최종명중 : {self.최종명중}\n')
        f.write(f'최종회피 : {self.최종회피}\n')
        f.write(f'최종치명타 : {self.최종치명타}\n')
        f.write(f'최종치명타증폭 : {self.최종치명타증폭}\n')
        f.write(f'최종방어력 : {self.최종방어력}\n')
        f.write(f'최종내성 : {self.최종내성}\n')
        f.write(f'최종회복 : {self.최종회복}\n')
        f.write(f'최종속도 : {self.최종속도}\n')
        f.write(f'경험치 : {self.경험치}\n')
        f.write(f'필요경험치 : {self.필요경험치}\n')
        f.write(f'코인 : {self.코인}\n')
        f.write(f'인벤토리_소유캐릭터이름 : {self.인벤토리.소유캐릭터이름}\n')

        for i, 스킬 in enumerate(self.스킬리스트):
            f.write(f'스킬_{i}_이름 : {스킬.이름}\n')
            f.write(f'스킬_{i}_레벨 : {스킬.레벨}\n')
            f.write(f'스킬_{i}_등급 : {스킬.등급}\n')
            f.write(f'스킬_{i}_데미지 : {스킬.데미지}\n')
            f.write(f'스킬_{i}_유형 : {스킬.유형}\n')
            f.write(f'스킬_{i}_지속시간 : {스킬.지속시간}\n')
            f.write(f'스킬_{i}_증폭 : {스킬.증폭}\n')
            f.write(f'스킬_{i}_최고레벨 : {스킬.최고레벨}\n')

        f.write(f'무기_이름 : {self.무기.이름}\n')
        f.write(f'무기_유형 : {self.무기.유형}\n')
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
        f.write(f'무기_최고강화레벨 : {self.무기.최고강화레벨}\n')
        for key, value in self.무기.추가능력치.items():
            f.write(f'무기_추가능력치_{key} : {value}\n')
        for i, 무기스킬 in enumerate(self.무기.무기스킬리스트):
            f.write(f'무기_스킬_{i}_이름 : {무기스킬.이름}\n')
            f.write(f'무기_스킬_{i}_레벨 : {무기스킬.레벨}\n')
            f.write(f'무기_스킬_{i}_등급 : {무기스킬.등급}\n')
            f.write(f'무기_스킬_{i}_데미지 : {무기스킬.데미지}\n')
            f.write(f'무기_스킬_{i}_유형 : {무기스킬.유형}\n')
            f.write(f'무기_스킬_{i}_지속시간 : {무기스킬.지속시간}\n')
            f.write(f'무기_스킬_{i}_증폭 : {무기스킬.증폭}\n')
            f.write(f'무기_스킬_{i}_최고레벨 : {무기스킬.최고레벨}\n')

        if self.갑옷:
            f.write(f'갑옷_이름 : {self.갑옷.이름}\n')
            f.write(f'갑옷_유형 : {self.갑옷.유형}\n')
            f.write(f'갑옷_등급 : {self.갑옷.등급}\n')
            f.write(f'갑옷_등급이름 : {self.갑옷.등급이름}\n')
            f.write(f'갑옷_강화레벨 : {self.갑옷.강화레벨}\n')
            f.write(f'갑옷_방어력 : {self.갑옷.방어력}\n')
            f.write(f'갑옷_HP : {self.갑옷.HP}\n')
            f.write(f'갑옷_내성 : {self.갑옷.내성}\n')
            f.write(f'갑옷_명중 : {self.갑옷.명중}\n')
            f.write(f'갑옷_회피 : {self.갑옷.회피}\n')
            f.write(f'갑옷_강화방어력 : {self.갑옷.강화방어력}\n')
            f.write(f'갑옷_강화HP : {self.갑옷.강화HP}\n')
            f.write(f'갑옷_강화내성 : {self.갑옷.강화내성}\n')
            f.write(f'갑옷_강화명중 : {self.갑옷.강화명중}\n')
            f.write(f'갑옷_강화회피 : {self.갑옷.강화회피}\n')
            f.write(f'갑옷_최종방어력 : {self.갑옷.최종방어력}\n')
            f.write(f'갑옷_최종HP : {self.갑옷.최종HP}\n')
            f.write(f'갑옷_최종내성 : {self.갑옷.최종내성}\n')
            f.write(f'갑옷_최종명중 : {self.갑옷.최종명중}\n')
            f.write(f'갑옷_최종회피 : {self.갑옷.최종회피}\n')
            for key, value in self.갑옷.추가능력치.items():
                f.write(f'갑옷_추가능력치_{key} : {value}\n')

        for i, 아이템 in enumerate(self.인벤토리.목록):
            if self.인벤토리.목록[i] == None: continue
            if 아이템.유형 == '무기':
                f.write(f'아이템_{i}_{아이템.유형}_id : {아이템.id}\n')
                f.write(f'아이템_{i}_{아이템.유형}_이름 : {아이템.이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_유형 : {아이템.유형}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급 : {아이템.등급}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급이름 : {아이템.등급이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화레벨 : {아이템.강화레벨}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최고강화레벨 : {아이템.최고강화레벨}\n')
                f.write(f'아이템_{i}_{아이템.유형}_인벤토리인덱스 : {i}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최소데미지 : {아이템.최소데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최대데미지 : {아이템.최대데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_증폭 : {아이템.증폭}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화최소데미지 : {아이템.강화최소데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화최대데미지 : {아이템.강화최대데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화증폭 : {아이템.강화증폭}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종최소데미지 : {아이템.최종최소데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종최대데미지 : {아이템.최종최대데미지}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종증폭 : {아이템.최종증폭}\n')
                for key, value in 아이템.추가능력치.items():
                    f.write(f'아이템_{i}_{아이템.유형}_추가능력치_{key} : {value}\n')
                for j, 스킬 in enumerate(아이템.무기스킬리스트):
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_이름 : {스킬.이름}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_레벨 : {스킬.레벨}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_등급 : {스킬.등급}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_데미지 : {스킬.데미지}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_유형 : {스킬.유형}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_지속시간 : {스킬.지속시간}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_증폭 : {스킬.증폭}\n')
                    f.write(f'아이템_{i}_{아이템.유형}_스킬_{j}_최고레벨 : {스킬.최고레벨}\n')
            elif 아이템.유형 == '갑옷':
                f.write(f'아이템_{i}_{아이템.유형}_id : {아이템.id}\n')
                f.write(f'아이템_{i}_{아이템.유형}_이름 : {아이템.이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_유형 : {아이템.유형}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급 : {아이템.등급}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급이름 : {아이템.등급이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화레벨 : {아이템.강화레벨}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최고강화레벨 : {아이템.최고강화레벨}\n')
                f.write(f'아이템_{i}_{아이템.유형}_인벤토리인덱스 : {i}\n')
                f.write(f'아이템_{i}_{아이템.유형}_방어력 : {아이템.방어력}\n')
                f.write(f'아이템_{i}_{아이템.유형}_HP : {아이템.HP}\n')
                f.write(f'아이템_{i}_{아이템.유형}_내성 : {아이템.내성}\n')
                f.write(f'아이템_{i}_{아이템.유형}_명중 : {아이템.명중}\n')
                f.write(f'아이템_{i}_{아이템.유형}_회피 : {아이템.회피}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화방어력 : {아이템.강화방어력}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화HP : {아이템.강화HP}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화내성 : {아이템.강화내성}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화명중 : {아이템.강화명중}\n')
                f.write(f'아이템_{i}_{아이템.유형}_강화회피 : {아이템.강화회피}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종방어력 : {아이템.최종방어력}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종HP : {아이템.최종HP}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종내성 : {아이템.최종내성}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종명중 : {아이템.최종명중}\n')
                f.write(f'아이템_{i}_{아이템.유형}_최종회피 : {아이템.최종회피}\n')
                for key, value in 아이템.추가능력치.items():
                    f.write(f'아이템_{i}_{아이템.유형}_추가능력치_{key} : {value}\n')
            elif type(아이템) == 소비:
                f.write(f'아이템_{i}_{아이템.유형}_id : {아이템.id}\n')
                f.write(f'아이템_{i}_{아이템.유형}_이름 : {아이템.이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급 : {아이템.등급}\n')
                f.write(f'아이템_{i}_{아이템.유형}_등급이름 : {아이템.등급이름}\n')
                f.write(f'아이템_{i}_{아이템.유형}_인벤토리인덱스 : {i}\n')
                f.write(f'아이템_{i}_{아이템.유형}_유형 : {아이템.유형}\n')
                f.write(f'아이템_{i}_{아이템.유형}_개수 : {아이템.개수}\n')
                
        f.close()

    def 불러오기(self, 캐릭터이름):
        if not os.path.isfile(f'./save/{캐릭터이름}.info'):
            raise(NameError)
        f = open(f'./save/{캐릭터이름}.info', 'r')
        캐릭터정보리스트 = []
        스킬딕셔너리 = {}
        무기스킬딕셔너리 = {}
        아이템딕셔너리 = {}
        아이템스킬딕셔너리 = {}
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            line_list = line.split(' : ')
            key_list = line_list[0].split('_')
            value = line_list[1]
            캐릭터정보리스트.append((key_list, value))

        장착장비세트 = set()
        for key_list, value in 캐릭터정보리스트:
            if key_list[0] == '갑옷': 장착장비세트.add('갑옷')
        for 장착장비 in 장착장비세트:
            if 장착장비=='갑옷': self.갑옷 = 갑옷('임시갑옷')

        for key_list, value in 캐릭터정보리스트:
            if len(key_list) == 1:
                if   key_list[0] == '이름': self.이름 = value
                elif key_list[0] == '레벨': self.레벨 = int(value)
                elif key_list[0] == '직업': self.직업 = value
                elif key_list[0] == 'STR':  self.STR  = int(value)
                elif key_list[0] == 'DEX':  self.DEX  = int(value)
                elif key_list[0] == 'INT':  self.INT  = int(value)
                elif key_list[0] == 'CON':  self.CON  = int(value)
                elif key_list[0] == 'LUK':  self.LUK  = int(value)
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
                elif key_list[0] == '추가STR':  self.추가STR  = int(value)
                elif key_list[0] == '추가DEX':  self.추가DEX  = int(value)
                elif key_list[0] == '추가INT':  self.추가INT  = int(value)
                elif key_list[0] == '추가CON':  self.추가CON  = int(value)
                elif key_list[0] == '추가LUK':  self.추가LUK  = int(value)
                elif key_list[0] == '추가공격력': self.추가공격력 = int(value)
                elif key_list[0] == '추가HP': self.추가HP = int(value)
                elif key_list[0] == '추가MP': self.추가MP = int(value)
                elif key_list[0] == '추가명중': self.추가명중 = int(value)
                elif key_list[0] == '추가회피': self.추가회피 = float(value)
                elif key_list[0] == '추가치명타': self.추가치명타 = float(value)
                elif key_list[0] == '추가치명타증폭': self.추가치명타증폭 = float(value)
                elif key_list[0] == '추가방어력': self.추가방어력 = int(value)
                elif key_list[0] == '추가내성': self.추가내성 = float(value)
                elif key_list[0] == '추가회복': self.추가회복 = int(value)
                elif key_list[0] == '추가속도': self.추가속도 = int(value)
                elif key_list[0] == '최종STR':  self.최종STR  = int(value)
                elif key_list[0] == '최종DEX':  self.최종DEX  = int(value)
                elif key_list[0] == '최종INT':  self.최종INT  = int(value)
                elif key_list[0] == '최종CON':  self.최종CON  = int(value)
                elif key_list[0] == '최종LUK':  self.최종LUK  = int(value)
                elif key_list[0] == '최종공격력': self.최종공격력 = int(value)
                elif key_list[0] == '최종HP': self.최종HP = int(value)
                elif key_list[0] == '최종MP': self.최종MP = int(value)
                elif key_list[0] == '최종명중': self.최종명중 = int(value)
                elif key_list[0] == '최종회피': self.최종회피 = float(value)
                elif key_list[0] == '최종치명타': self.최종치명타 = float(value)
                elif key_list[0] == '최종치명타증폭': self.최종치명타증폭 = float(value)
                elif key_list[0] == '최종방어력': self.최종방어력 = int(value)
                elif key_list[0] == '최종내성': self.최종내성 = float(value)
                elif key_list[0] == '최종회복': self.최종회복 = int(value)
                elif key_list[0] == '최종속도': self.최종속도 = int(value)
                elif key_list[0] == '경험치': self.경험치 = int(value)
                elif key_list[0] == '필요경험치': self.필요경험치 = int(value)
                elif key_list[0] == '코인': self.코인 = int(value)
            elif len(key_list) >= 2:
                if key_list[0] == '인벤토리':
                    if key_list[1] == '소유캐릭터이름': self.인벤토리.소유캐릭터이름 = value
                elif key_list[0] == '무기':
                    if   key_list[1] == '이름': self.무기.이름 = value
                    elif key_list[1] == '등급': self.무기.등급 = int(value)
                    elif key_list[1] == '등급이름': self.무기.등급이름 = value
                    elif key_list[1] == '강화레벨': self.무기.강화레벨 = int(value)
                    elif key_list[1] == '최고강화레벨': self.무기.최고강화레벨 = int(value)
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
                    elif key_list[1] == '스킬':
                        if key_list[2] not in 무기스킬딕셔너리:
                            무기스킬딕셔너리[key_list[2]] = {key_list[3]: value}
                        else:
                            무기스킬딕셔너리[key_list[2]][key_list[3]] = value
                elif key_list[0] == '갑옷':
                    if   key_list[1] == '이름': self.갑옷.이름 = value
                    elif key_list[1] == '등급': self.갑옷.등급 = int(value)
                    elif key_list[1] == '등급이름': self.갑옷.등급이름 = value
                    elif key_list[1] == '강화레벨': self.갑옷.강화레벨 = int(value)
                    elif key_list[1] == '최고강화레벨': self.갑옷.최고강화레벨 = int(value)
                    elif key_list[1] == '방어력': self.갑옷.방어력 = int(value)
                    elif key_list[1] == 'HP': self.갑옷.HP = int(value)
                    elif key_list[1] == '내성': self.갑옷.내성 = float(value)
                    elif key_list[1] == '명중': self.갑옷.명중 = int(value)
                    elif key_list[1] == '회피': self.갑옷.회피 = float(value)
                    elif key_list[1] == '강화방어력': self.갑옷.강화방어력 = int(value)
                    elif key_list[1] == '강화HP': self.갑옷.강화HP = int(value)
                    elif key_list[1] == '강화내성': self.갑옷.강화내성 = float(value)
                    elif key_list[1] == '강화명중': self.갑옷.강화명중 = int(value)
                    elif key_list[1] == '강화회피': self.갑옷.강화회피 = float(value)
                    elif key_list[1] == '최종방어력': self.갑옷.최종방어력 = int(value)
                    elif key_list[1] == '최종HP': self.갑옷.최종HP = int(value)
                    elif key_list[1] == '최종내성': self.갑옷.최종내성 = float(value)
                    elif key_list[1] == '최종명중': self.갑옷.최종명중 = int(value)
                    elif key_list[1] == '최종회피': self.갑옷.최종회피 = float(value)
                    elif key_list[1] == '추가능력치':
                        if   key_list[2] == 'STR': self.갑옷.추가능력치['STR'] = int(value)
                        elif key_list[2] == 'DEX': self.갑옷.추가능력치['DEX'] = int(value)
                        elif key_list[2] == 'INT': self.갑옷.추가능력치['INT'] = int(value)
                        elif key_list[2] == 'CON': self.갑옷.추가능력치['CON'] = int(value)
                        elif key_list[2] == 'LUK': self.갑옷.추가능력치['LUK'] = int(value)
                elif key_list[0] == '스킬':
                    if key_list[1] not in 스킬딕셔너리:
                        스킬딕셔너리[key_list[1]] = {key_list[2]: value}
                    else:
                        스킬딕셔너리[key_list[1]][key_list[2]] = value
                elif key_list[0] == '아이템':
                    if key_list[1] not in 아이템딕셔너리:
                        아이템딕셔너리[key_list[1]] = {'유형': key_list[2]}
                        if key_list[3] == '스킬':
                            if key_list[4] not in 아이템스킬딕셔너리:
                                아이템스킬딕셔너리[key_list[4]] = {key_list[5]: value}
                            else:
                                아이템스킬딕셔너리[key_list[4]][key_list[5]] = value
                            아이템딕셔너리[key_list[1]][key_list[3]] = 아이템스킬딕셔너리
                        else:
                            if key_list[3] == '추가능력치':
                                if key_list[3] not in 아이템딕셔너리[key_list[1]]:
                                    아이템딕셔너리[key_list[1]][key_list[3]] = {key_list[4]: value}
                                else:
                                    아이템딕셔너리[key_list[1]][key_list[3]][key_list[4]] = value
                            else:
                                아이템딕셔너리[key_list[1]] = {key_list[3]: value}
                    else:
                        if key_list[3] == '스킬':
                            if key_list[4] not in 아이템스킬딕셔너리:
                                아이템스킬딕셔너리[key_list[4]] = {key_list[5]: value}
                            else:
                                아이템스킬딕셔너리[key_list[4]][key_list[5]] = value
                            아이템딕셔너리[key_list[1]][key_list[3]] = 아이템스킬딕셔너리
                        else:
                            if key_list[3] == '추가능력치':
                                if key_list[3] not in 아이템딕셔너리[key_list[1]]:
                                    아이템딕셔너리[key_list[1]][key_list[3]] = {key_list[4]: value}
                                else:
                                    아이템딕셔너리[key_list[1]][key_list[3]][key_list[4]] = value
                            else:
                                아이템딕셔너리[key_list[1]][key_list[3]] = value
        for key1 in 스킬딕셔너리.keys():
            임시스킬 = 스킬('임시스킬')
            for key2, value in 스킬딕셔너리[key1].items():
                if   key2 == '이름': 임시스킬.이름 = value
                elif key2 == '레벨': 임시스킬.레벨 = int(value)
                elif key2 == '등급': 임시스킬.등급 = int(value)
                elif key2 == '데미지': 임시스킬.데미지 = int(value)
                elif key2 == '유형': 임시스킬.유형 = value
                elif key2 == '지속시간': 임시스킬.지속시간 = int(value)
                elif key2 == '증폭': 임시스킬.증폭 = float(value)
                elif key2 == '최고레벨': 임시스킬.최고레벨 = int(value)
            if 임시스킬.이름 != '임시스킬':
                self.스킬리스트.append(임시스킬)

        for key1 in 무기스킬딕셔너리.keys():
            임시무기스킬 = 스킬('임시무기스킬')
            for key2, value in 무기스킬딕셔너리[key1].items():
                if   key2 == '이름': 임시무기스킬.이름 = value
                elif key2 == '레벨': 임시무기스킬.레벨 = int(value)
                elif key2 == '등급': 임시무기스킬.등급 = int(value)
                elif key2 == '데미지': 임시무기스킬.데미지 = int(value)
                elif key2 == '유형': 임시무기스킬.유형 = value
                elif key2 == '지속시간': 임시무기스킬.지속시간 = int(value)
                elif key2 == '증폭': 임시무기스킬.증폭 = float(value)
                elif key2 == '최고레벨': 임시무기스킬.최고레벨 = int(value)
            if 임시무기스킬.이름 != '임시무기스킬':
                self.무기.무기스킬리스트.append(임시무기스킬)

        for key1 in 아이템딕셔너리.keys():
            인벤토리인덱스 = -1
            if 아이템딕셔너리[key1]['유형'] == '무기':
                임시무기 = 무기('임시무기')
                for key2, value in 아이템딕셔너리[key1].items():
                    if   key2 == 'id': 임시무기.id = value
                    elif key2 == '이름': 임시무기.이름 = value
                    elif key2 == '등급': 임시무기.등급 = int(value)
                    elif key2 == '등급이름': 임시무기.등급이름 = value
                    elif key2 == '인벤토리인덱스': 인벤토리인덱스 = int(value)
                    elif key2 == '유형': 임시무기.유형 = value
                    elif key2 == '강화레벨': 임시무기.강화레벨 = int(value)
                    elif key2 == '최고강화레벨': 임시무기.최고강화레벨 = int(value)
                    elif key2 == '최소데미지': 임시무기.최소데미지 = int(value)
                    elif key2 == '최대데미지': 임시무기.최대데미지 = int(value)
                    elif key2 == '증폭': 임시무기.증폭 = float(value)
                    elif key2 == '강화최소데미지': 임시무기.강화최소데미지 = int(value)
                    elif key2 == '강화최대데미지': 임시무기.강화최대데미지 = int(value)
                    elif key2 == '강화증폭': 임시무기.강화증폭 = float(value)
                    elif key2 == '최종최소데미지': 임시무기.최종최소데미지 = int(value)
                    elif key2 == '최종최대데미지': 임시무기.최종최대데미지 = int(value)
                    elif key2 == '최종증폭': 임시무기.최종증폭 = float(value)
                    elif key2 == '추가능력치':
                        for key3, value2 in value.items():
                            if   key3 == 'STR': 임시무기.추가능력치['STR'] = int(value2)
                            elif key3 == 'DEX': 임시무기.추가능력치['DEX'] = int(value2)
                            elif key3 == 'INT': 임시무기.추가능력치['INT'] = int(value2)
                            elif key3 == 'CON': 임시무기.추가능력치['CON'] = int(value2)
                            elif key3 == 'LUK': 임시무기.추가능력치['LUK'] = int(value2)
                    elif key2 == '스킬':
                        임시스킬 = 스킬('임시스킬')
                        for value_dict in 아이템딕셔너리[key1]['스킬'].values():    # 아이템스킬딕셔너리
                            for key3, value in value_dict.items():
                                if   key3 == '이름': 임시스킬.이름 = value
                                elif key3 == '레벨': 임시스킬.레벨 = int(value)
                                elif key3 == '등급': 임시스킬.등급 = int(value)
                                elif key3 == '데미지': 임시스킬.데미지 = int(value)
                                elif key3 == '유형': 임시스킬.유형 = value
                                elif key3 == '지속시간': 임시스킬.지속시간 = int(value)
                                elif key3 == '증폭': 임시스킬.증폭 = float(value)
                                elif key3 == '최고레벨': 임시스킬.최고레벨 = int(value)
                        if 임시스킬.이름 != '임시스킬':
                            임시무기.무기스킬리스트.append(임시스킬)

                if 임시무기.이름 != '임시무기' and 인벤토리인덱스 != -1:
                    self.인벤토리.추가_인덱스(임시무기, 인벤토리인덱스)

            elif 아이템딕셔너리[key1]['유형'] == '갑옷':
                임시갑옷 = 갑옷('임시갑옷')
                for key2, value in 아이템딕셔너리[key1].items():
                    if   key2 == 'id': 임시갑옷.id = value
                    elif key2 == '이름': 임시갑옷.이름 = value
                    elif key2 == '등급': 임시갑옷.등급 = int(value)
                    elif key2 == '등급이름': 임시갑옷.등급이름 = value
                    elif key2 == '인벤토리인덱스': 인벤토리인덱스 = int(value)
                    elif key2 == '유형': 임시갑옷.유형 = value
                    elif key2 == '강화레벨': 임시갑옷.강화레벨 = int(value)
                    elif key2 == '최고강화레벨': 임시갑옷.최고강화레벨 = int(value)
                    elif key2 == '방어력': 임시갑옷.방어력 = int(value)
                    elif key2 == 'HP': 임시갑옷.HP = int(value)
                    elif key2 == '내성': 임시갑옷.내성 = float(value)
                    elif key2 == '명중': 임시갑옷.명중 = int(value)
                    elif key2 == '회피': 임시갑옷.회피 = float(value)
                    elif key2 == '강화방어력': 임시갑옷.강화방어력 = int(value)
                    elif key2 == '강화HP': 임시갑옷.강화HP = int(value)
                    elif key2 == '강화내성': 임시갑옷.강화내성 = float(value)
                    elif key2 == '강화명중': 임시갑옷.강화명중 = int(value)
                    elif key2 == '강화회피': 임시갑옷.강화회피 = float(value)
                    elif key2 == '최종방어력': 임시갑옷.최종방어력 = int(value)
                    elif key2 == '최종HP': 임시갑옷.최종HP = int(value)
                    elif key2 == '최종내성': 임시갑옷.최종내성 = float(value)
                    elif key2 == '최종명중': 임시갑옷.최종명중 = int(value)
                    elif key2 == '최종회피': 임시갑옷.최종회피 = float(value)
                    elif key2 == '추가능력치':
                        for key3, value2 in value.items():
                            if   key3 == 'STR': 임시갑옷.추가능력치['STR'] = int(value2)
                            elif key3 == 'DEX': 임시갑옷.추가능력치['DEX'] = int(value2)
                            elif key3 == 'INT': 임시갑옷.추가능력치['INT'] = int(value2)
                            elif key3 == 'CON': 임시갑옷.추가능력치['CON'] = int(value2)
                            elif key3 == 'LUK': 임시갑옷.추가능력치['LUK'] = int(value2)

            elif 아이템딕셔너리[key1]['유형'] == '주문서':
                임시소비 = 소비('임시소비', '주문서')
                for key2, value in 아이템딕셔너리[key1].items():
                    if   key2 == 'id': 임시소비.id = value
                    elif key2 == '이름': 임시소비.이름 = value
                    elif key2 == '등급': 임시소비.등급 = int(value)
                    elif key2 == '등급이름': 임시소비.등급이름 = value
                    elif key2 == '인벤토리인덱스': 인벤토리인덱스 = int(value)
                    elif key2 == '유형': 임시소비.유형 = value
                    elif key2 == '개수': 임시소비.개수 = int(value)

                if 임시소비.이름 != '임시소비' and 인벤토리인덱스 != -1:
                    self.인벤토리.추가_인덱스(임시소비, 인벤토리인덱스)
            
        f.close()
        마을.저장(self)
        return self
        
    def 아이템구매(self, 아이템):
        인벤토리인덱스, 인벤토리아이템 = self.인벤토리.이름으로찾기(아이템.이름)
        if not 인벤토리아이템:
            인벤토리인덱스 = self.인벤토리.추가(아이템)
            self.인벤토리.목록[인벤토리인덱스].개수 += 1
        else:
            인벤토리아이템.개수 += 1
        self.저장()
        return 인벤토리인덱스

    def 아이템판매(self, 인벤토리인덱스, 개수=1):
        인벤토리아이템 = self.인벤토리.목록[인벤토리인덱스]
        if 인벤토리아이템.유형 == '무기':
            인벤토리.제거(인벤토리인덱스)
        elif type(인벤토리아이템) == 소비:
            if 인벤토리아이템.개수 > 개수:
                인벤토리아이템.개수 -= 개수
            else:
                인벤토리.제거(인벤토리인덱스)
