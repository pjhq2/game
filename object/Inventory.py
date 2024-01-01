from master import gprint
from master import calc_str_length

class 인벤토리():
    def __init__(self, 소유캐릭터이름):
        self.소유캐릭터이름 = 소유캐릭터이름
        self.목록 = [None for _ in range(40)]

    def 추가(self, 아이템):
        빈공간인덱스 = self.빈공간인덱스()
        self.목록[빈공간인덱스] = 아이템
        self.모두출력()
    
    def 추가_인덱스(self, 아이템, 인덱스):
        self.목록[인덱스] = 아이템
        self.모두출력()

    def 제거(self, 인덱스):
        if self.목록[인덱스] == None:
            return
        self.목록[인덱스] = None
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
        print(f'(+{self.목록[인덱스].강화레벨})')

    def 모두출력(self):
        header = f'========== {self.소유캐릭터이름}의 인벤토리 =========='
        footer = '=' * calc_str_length(header)
        print(header)
        for 인덱스 in range(len(self.목록)):
            self.출력(인덱스)
        print(footer)
