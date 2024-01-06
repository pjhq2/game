import random

from system.master import gprint
from system.master import trunc
from system.master import calc_str_length

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

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨   += 1
        self.강화방어력 += self.등급*2 + 5
        self.강화HP     += self.등급*5 + 10
        if self.강화레벨 % 2:
            self.강화회복 += (self.등급+2)*2
        self.최종방어력 = self.방어력 + self.강화방어력
        self.최종HP     = self.HP     + self.강화HP
        self.최종회복   = self.회복   + self.강화회복
    
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
        print(f' 회복   : {self.회복}(+{self.강화회복})')
        print(f'------------------------------')

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
        self.최종방어력 = self.방어력 + self.강화방어력
        self.최종HP     = self.HP     + self.강화HP
        self.최종내성   = self.내성   + self.강화내성
        self.최종명중   = self.명중   + self.강화명중
        self.최종회피   = self.회피   + self.강화회피
    
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

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨   += 1
        self.강화방어력 += self.등급*2 + 5
        if self.강화레벨 % 2:
            if 파라미터 <= 50:
                self.강화내성 += (self.등급+4)*0.001
        else:
            self.강화명중 += self.등급*3 + 3
        self.최종방어력 = self.방어력 + self.강화방어력
        self.최종내성   = self.내성   + self.강화내성
        self.최종명중   = self.명중   + self.강화명중
    
    def 출력(self):
        print(f'------------------------------')
        gprint(f'{self.이름}', self.등급, end='')
        print(f'(+{self.강화레벨})')
        print(' '*(29-calc_str_length(self.유형)) + self.유형)
        print(f' 등급   : {self.등급이름}')
        for key, value in self.추가능력치.items():
            print(f' {key}    : +{value}')
        print(f' 방어력 : {self.방어력}(+{self.강화방어력})')
        print(f' 내성   : {trunc(self.내성, 2)}(+{trunc(self.강화내성, 2)})')
        print(f' 명중   : {self.명중}(+{self.강화명중})')
        print(f'------------------------------')

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

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨   += 1
        self.강화방어력 += self.등급*2 + 5
        if self.강화레벨 % 2:
            self.강화회피 += (self.등급+2)*0.001
            if 파라미터 <= 50:
                self.강화속도 += (self.등급+4)
        self.최종방어력 = self.방어력 + self.강화방어력
        self.최종회피   = self.회피   + self.강화회피
        self.최종속도   = self.속도   + self.강화속도
    
    def 출력(self):
        print(f'------------------------------')
        gprint(f'{self.이름}', self.등급, end='')
        print(f'(+{self.강화레벨})')
        print(' '*(29-calc_str_length(self.유형)) + self.유형)
        print(f' 등급   : {self.등급이름}')
        for key, value in self.추가능력치.items():
            print(f' {key}    : +{value}')
        print(f' 방어력 : {self.방어력}(+{self.강화방어력})')
        print(f' 회피   : {trunc(self.회피, 2)}(+{trunc(self.강화회피, 2)})')
        print(f' 속도   : {self.속도}(+{self.강화속도})')
        print(f'------------------------------')

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

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨       += 1
        self.강화치명타     += self.등급*0.001
        self.강화치명타증폭 += (self.등급+1)*0.005
        if self.강화레벨 % 2:
            self.강화치명타증폭 += (self.등급+1)*0.005
        self.최종치명타     = self.치명타     + self.강화치명타
        self.최종치명타증폭 = self.치명타증폭 + self.강화치명타증폭
    
    def 출력(self):
        print(f'------------------------------')
        gprint(f'{self.이름}', self.등급, end='')
        print(f'(+{self.강화레벨})')
        print(' '*(29-calc_str_length(self.유형)) + self.유형)
        print(f' 등급       : {self.등급이름}')
        for key, value in self.추가능력치.items():
            print(f' {key}        : +{value}')
        print(f' 치명타     : {trunc(self.치명타, 2)}(+{trunc(self.강화치명타, 2)})')
        print(f' 치명타증폭 : {trunc(self.치명타증폭, 2)}(+{trunc(self.강화치명타증폭, 2)})')
        print(f'------------------------------')

def 철투구():
    철투구 = 모자('철투구')
    철투구.등급 = 3
    철투구.등급이름 = '희귀'
    철투구.추가능력치['STR'] = 2
    철투구.추가능력치['DEX'] = 3
    철투구.추가능력치['CON'] = 4
    제작등급 = random.randint(1, 100)
    if 제작등급 <= 20:
        철투구.방어력 = 95
        철투구.HP     = 200
        철투구.회복   = 15
    else:
        철투구.방어력 = random.randint(85, 94)
        철투구.HP     = random.randint(150, 199)
        철투구.회복   = random.randint(10, 14)
    철투구.초기세팅()
    return 철투구

def 철갑옷():
    철갑옷 = 갑옷('철갑옷')
    철갑옷.등급 = 3
    철갑옷.등급이름 = '희귀'
    철갑옷.추가능력치['STR'] = 3
    철갑옷.추가능력치['DEX'] = 3
    철갑옷.추가능력치['CON'] = 3
    제작등급 = random.randint(1, 100)
    if 제작등급 <= 20:
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

def 철장갑():
    철장갑 = 장갑('철장갑')
    철장갑.등급 = 3
    철장갑.등급이름 = '희귀'
    철장갑.추가능력치['STR'] = 5
    철장갑.추가능력치['DEX'] = 2
    철장갑.추가능력치['CON'] = 1
    제작등급 = random.randint(1, 100)
    if 제작등급 <= 20:
        철장갑.방어력 = 95
        철장갑.내성   = 0.05
        철장갑.명중   = 10
    else:
        철장갑.방어력 = random.randint(85, 94)
        철장갑.내성   = random.randint(1, 4)/100
        철장갑.명중   = random.randint(6, 9)
    철장갑.초기세팅()
    return 철장갑

def 철신발():
    철신발 = 신발('철신발')
    철신발.등급 = 3
    철신발.등급이름 = '희귀'
    철신발.추가능력치['STR'] = 1
    철신발.추가능력치['DEX'] = 5
    철신발.추가능력치['CON'] = 3
    제작등급 = random.randint(1, 100)
    if 제작등급 <= 20:
        철신발.방어력 = 95
        철신발.회피   = 0.05
        철신발.속도   = 10
    else:
        철신발.방어력 = random.randint(85, 94)
        철신발.회피   = random.randint(1, 4)/100
        철신발.속도   = random.randint(6, 9)
    철신발.초기세팅()
    return 철신발

def 태초의정신():
    태초의정신 = 코어('태초의정신')
    태초의정신.등급 = 2
    태초의정신.등급이름 = '고급'
    if random.randint(1, 100) <= 60: 태초의정신.추가능력치['STR'] = 1
    if random.randint(1, 100) <= 60: 태초의정신.추가능력치['DEX'] = 1
    if random.randint(1, 100) <= 60: 태초의정신.추가능력치['INT'] = 1
    if random.randint(1, 100) <= 60: 태초의정신.추가능력치['CON'] = 1
    if random.randint(1, 100) <= 60: 태초의정신.추가능력치['LUK'] = 1
    제작등급 = random.randint(1, 100)
    if 제작등급 <= 20:
        태초의정신.치명타     = 0.1
        태초의정신.치명타증폭 = 0.1
    else:
        태초의정신.치명타     = random.randint(6, 9)/100
        태초의정신.치명타증폭 = random.randint(6, 9)/100
    태초의정신.초기세팅()
    return 태초의정신
