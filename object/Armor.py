import random

from master import gprint
from master import trunc
from master import calc_str_length

from .Item  import 장비아이템

class 모자(장비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.유형           = '모자'
        self.방어력         = 0
        self.HP             = 0
        self.회복           = 0
        self.강화방어력     = 0
        self.강화HP         = 0
        self.강화회복       = 0
        self.최종방어력     = 0
        self.최종HP         = 0
        self.최종회복       = 0
        self.추가능력치     = {}
    
    def 초기세팅(self):
        self.최종방어력 = self.방어력
        self.최종HP     = self.HP
        self.최종회복   = self.회복

class 갑옷(장비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.유형           = '갑옷'
        self.방어력         = 0
        self.HP             = 0
        self.내성           = 0
        self.명중           = 0
        self.회피           = 0
        self.강화방어력     = 0
        self.강화HP         = 0
        self.강화내성       = 0
        self.강화명중       = 0
        self.강화회피       = 0
        self.최종방어력     = 0
        self.최종HP         = 0
        self.최종내성       = 0
        self.최종명중       = 0
        self.최종회피       = 0
        self.추가능력치     = {}

    def 초기세팅(self):
        self.최종방어력 = self.방어력
        self.최종HP     = self.HP
        self.최종내성   = self.내성
        self.최종명중   = self.최종명중
        self.최종회피   = self.최종회피

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨   += 1
        self.강화방어력 += self.등급*2 + 5
        self.강화HP     += self.등급*5 + 10
        if self.강화레벨 % 2:
            self.강화회피 += (self.등급+2)*0.001
            if 파라미터 <= 50:
                self.강화내성 += (self.등급+4)*0.001
        else:
            self.강화명중 += self.등급*3 + 3
        self.최종방어력 = self.방어력 + self.최종방어력
        self.최종HP     = self.HP     + self.최종HP
        self.최종내성   = self.내성   + self.최종내성
        self.최종명중   = self.명중   + self.최종명중
        self.최종회피   = self.회피   + self.최종회피
    
    def 출력(self):
        print(f'------------------------------')
        gprint(f'{self.이름}', self.등급, end='')
        print(f'(+{self.강화레벨})')
        print(' '*(29-calc_str_length(self.유형)) + self.유형)
        print(f' 등급   : {self.등급이름}')
        for key, value in self.추가능력치.items():
            print(f' {key}    : +{value}')
        print(f' 방어력 : {self.방어력}(+{self.강화방어력})')
        print(f' HP     : {self.HP}(+{self.강화HP})')
        print(f' 내성   : {trunc(self.내성, 2)}(+{trunc(self.강화내성, 2)})')
        print(f' 명중   : {self.명중}(+{self.강화명중})')
        print(f' 회피   : {trunc(self.회피, 2)}(+{trunc(self.강화회피, 2)})')
        print(f'------------------------------')

class 장갑(장비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.유형           = '장갑'
        self.방어력         = 0
        self.내성           = 0
        self.명중           = 0
        self.강화방어력     = 0
        self.강화내성       = 0
        self.강화명중       = 0
        self.최종방어력     = 0
        self.최종내성       = 0
        self.최종명중       = 0
        self.추가능력치     = {}

    def 초기세팅(self):
        self.최종방어력 = self.방어력
        self.최종명중   = self.명중
        self.최종내성   = self.내성

class 신발(장비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.유형           = '신발'
        self.방어력         = 0
        self.회피           = 0
        self.속도           = 0
        self.강화방어력     = 0
        self.강화회피       = 0
        self.강화속도       = 0
        self.최종방어력     = 0
        self.최종회피       = 0
        self.최종속도       = 0
        self.추가능력치     = {}

    def 초기세팅(self):
        self.최종방어력 = self.방어력
        self.최종회피   = self.회피
        self.최종속도   = self.속도

class 코어(장비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.유형           = '코어'
        self.치명타         = 0
        self.치명타증폭     = 0
        self.강화치명타     = 0
        self.강화치명타증폭 = 0
        self.최종치명타     = 0
        self.최종치명타증폭 = 0
        self.추가능력치     = {}
    
    def 초기세팅(self):
        self.최종치명타     = self.치명타
        self.최종치명타증폭 = self.치명타증폭

def 제작_철갑옷():
    철갑옷 = 갑옷('철갑옷')
    철갑옷.등급 = 3
    철갑옷.등급이름 = '희귀'
    철갑옷.추가능력치['STR'] = 2
    철갑옷.추가능력치['DEX'] = 2
    철갑옷.추가능력치['CON'] = 2
    철갑옷.추가능력치['INT'] = 2
    철갑옷.추가능력치['LUK'] = 2
    데미지등급 = random.randint(1, 100)
    if 데미지등급 <= 20:
        철갑옷.방어력 = 95
        철갑옷.HP     = 200
        철갑옷.내성   = 0.05
        철갑옷.명중   = 10
        철갑옷.회피   = 0.05
    else:
        철갑옷.방어력 = random.randint(85, 94)
        철갑옷.HP     = random.randint(150, 199)
        철갑옷.내성   = random.randint(1, 4)/100
        철갑옷.명중   = random.randint(6, 9)
        철갑옷.회피   = random.randint(3, 4)/100
    철갑옷.초기세팅()
    return 철갑옷
