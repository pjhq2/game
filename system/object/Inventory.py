from master import gprint
from master import calc_str_length

from .Consumption import 소비

class 인벤토리():
    def __init__(self, 소유캐릭터이름):
        self.소유캐릭터이름 = 소유캐릭터이름
        self.목록 = [None for _ in range(40)]

    def 이름으로찾기(self, 아이템이름):
        for 인벤토리인덱스, 아이템 in enumerate(self.목록):
            if 아이템 == None: continue
            if 아이템.이름 == 아이템이름:
                return 인벤토리인덱스, 아이템
        return -1, None

    def 추가(self, 아이템, 개수=1):
        빈공간인덱스 = self.빈공간인덱스()
        self.목록[빈공간인덱스] = 아이템
        if type(아이템) == 소비:
            self.목록[빈공간인덱스].개수 += 개수
        self.모두출력()
        return 빈공간인덱스
    
    def 추가_인덱스(self, 아이템, 인덱스):
        self.목록[인덱스] = 아이템
        self.모두출력()

    def 제거(self, 인덱스):
        if self.목록[인덱스] == None:
            return
        self.목록[인덱스] = None
        self.모두출력()

    def 이동(self, 이전인덱스, 이후인덱스):
        if self.목록[이전인덱스] != None:
            self.목록[이전인덱스], self.목록[이후인덱스] = self.목록[이후인덱스], self.목록[이전인덱스]
            self.모두출력()
    
    def 빈공간인덱스(self):
        for 인덱스 in range(len(self.목록)):
            if self.목록[인덱스] == None:
                return 인덱스
        else:
            print('인벤토리가 가득 찼습니다.')

    def 아이템개수(self):
        개수 = 0
        for 인덱스 in range(len(self.목록)):
            if self.목록[인덱스] != None: 개수 += 1
        return 개수
    
    def 출력(self, 인덱스):
        if self.목록[인덱스] == None:
            return
        print(f'[{인덱스}] ', end='')
        gprint(f'{self.목록[인덱스].이름}', self.목록[인덱스].등급, end='')
        인벤토리길이   = calc_str_length(f'{self.소유캐릭터이름}의 인벤토리') + 22
        소비아이템길이 = calc_str_length(f'[{인덱스}] {self.목록[인덱스].이름}')
        if self.목록[인덱스].유형 == '무기' or \
           self.목록[인덱스].유형 == '모자' or \
           self.목록[인덱스].유형 == '갑옷' or \
           self.목록[인덱스].유형 == '장갑' or \
           self.목록[인덱스].유형 == '신발' or \
           self.목록[인덱스].유형 == '코어':
            print(f'(+{self.목록[인덱스].강화레벨})')
        elif type(self.목록[인덱스]) == 소비:
            print(' '*(인벤토리길이-소비아이템길이-1-len(str(self.목록[인덱스].개수))), end='')
            print(f'{self.목록[인덱스].개수}')

    def 모두출력(self):
        header = f'========== {self.소유캐릭터이름}의 인벤토리 =========='
        footer = '=' * calc_str_length(header)
        print(header)
        for 인덱스 in range(len(self.목록)):
            self.출력(인덱스)
        print(footer)
