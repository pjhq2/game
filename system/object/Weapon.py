import random

from system.master  import trunc
from system.master  import gprint
from system.master  import calc_str_length

from .Skill  import *
from .Item   import 장비아이템

class 무기(장비아이템):
    def __init__(self, 이름='주먹'):
        super().__init__(이름)
        self.유형           = '무기'
        self.최소데미지     = 0
        self.최대데미지     = 0
        self.증폭           = 1.0
        self.강화최소데미지 = 0
        self.강화최대데미지 = 0
        self.강화증폭       = 0
        self.최종최소데미지 = self.최소데미지
        self.최종최대데미지 = self.최대데미지
        self.최종증폭       = self.증폭
        self.추가능력치     = {}
        self.무기스킬리스트 = []

    def 초기세팅(self):
        self.최종최소데미지 = self.최소데미지
        self.최종최대데미지 = self.최대데미지
        self.최종증폭       = self.증폭

    def 강화레벨업(self):
        파라미터 = random.randint(1, 100)
        self.강화레벨 += 1
        if self.강화레벨 % 2:
            self.강화최소데미지 += self.등급 - 1
            self.강화최대데미지 += self.등급
            if 파라미터 <= 50:
                self.강화증폭       += self.강화레벨 * (self.등급 + 1) / 100
        else:
            self.강화최소데미지 += self.등급
            self.강화최대데미지 += self.등급
        self.최종최소데미지 = self.최소데미지 + self.강화최소데미지
        self.최종최대데미지 = self.최대데미지 + self.강화최대데미지
        self.최종증폭       = self.증폭       + self.강화증폭

    def 출력(self):
        print(f'------------------------------')
        gprint(f'{self.이름}', self.등급, end='')
        print(f'(+{self.강화레벨})')
        print(' '*(29-calc_str_length(self.유형)) + self.유형)
        print(f' 등급       : {self.등급이름}')
        for key, value in self.추가능력치.items():
            print(f' {key}        : +{value}')
        print(f' 최소데미지 : {self.최소데미지}(+{self.강화최소데미지})')
        print(f' 최대데미지 : {self.최대데미지}(+{self.강화최대데미지})')
        print(f' 증폭       : {trunc(self.증폭, 2)}(+{trunc(self.강화증폭, 2)})')
        print(f' 무기데미지 : {int(self.최종증폭*self.최종최소데미지)} - {int(self.최종증폭*self.최종최대데미지)}')
        if len(self.무기스킬리스트) >= 1:
            print(f' 무기스킬   : {self.무기스킬리스트[0].이름} Lv.{self.무기스킬리스트[0].레벨}')
            for 무기스킬 in self.무기스킬리스트[1:]:
                print(f'              {무기스킬.이름} Lv.{무기스킬.레벨}')
        print(f'------------------------------')

def 나무몽둥이():
    나무몽둥이 = 무기('나무몽둥이')
    나무몽둥이.등급 = 1
    나무몽둥이.등급이름 = '일반'
    나무몽둥이.추가능력치['DEX'] = 1
    나무몽둥이.무기스킬리스트.append(무기스킬_내려치기())
    데미지등급 = random.randint(1, 100)
    if 데미지등급 <= 20:
        나무몽둥이.최소데미지 = 1
        나무몽둥이.최대데미지 = 2
    else:
        나무몽둥이.최소데미지 = 0
        나무몽둥이.최대데미지 = 2
    나무몽둥이.초기세팅()
    return 나무몽둥이

def 진검():
    진검 = 무기('진검')
    진검.등급 = 2
    진검.등급이름 = '고급'
    진검.추가능력치['STR'] = 3
    데미지등급 = random.randint(1, 100)
    if 데미지등급 <= 20:
        진검.최소데미지 = 2
        진검.최대데미지 = 5
    else:
        진검.최소데미지 = 1
        진검.최대데미지 = 5
    진검.초기세팅()
    return 진검

def 글라디우스():
    글라디우스 = 무기('글라디우스')
    글라디우스.등급 = 3
    글라디우스.등급이름 = '희귀'
    글라디우스.추가능력치['STR'] = 2
    글라디우스.추가능력치['DEX'] = 1
    글라디우스.추가능력치['CON'] = 1
    글라디우스.추가능력치['LUK'] = 1
    데미지등급 = random.randint(1, 100)
    if 데미지등급 <= 20:
        글라디우스.최소데미지 = 13
        글라디우스.최대데미지 = 17
    else:
        글라디우스.최소데미지 = 12
        글라디우스.최대데미지 = 16
    글라디우스.초기세팅()
    return 글라디우스

def 참월():
    참월 = 무기('참월')
    참월.등급 = 4
    참월.등급이름 = '영웅'
    참월.추가능력치['STR'] = 12
    참월.무기스킬리스트.append(무기스킬_월아천충())
    데미지등급 = random.randint(1, 100)
    if 데미지등급 <= 20:
        참월.최소데미지 = 40
        참월.최대데미지 = 85
    elif 데미지등급 <= 80:
        참월.최소데미지 = 36
        참월.최대데미지 = 80
    else:
        참월.최소데미지 = 32
        참월.최대데미지 = 75
    참월.초기세팅()
    return 참월

def 엑스칼리버():
    엑스칼리버 = 무기('엑스칼리버')
    엑스칼리버.등급 = 5
    엑스칼리버.등급이름 = '전설'
    엑스칼리버.추가능력치['STR'] = 25
    엑스칼리버.추가능력치['DEX'] = 20
    엑스칼리버.무기스킬리스트.append(무기스킬_시동())
    최소데미지등급 = random.randint(1, 100)
    최대데미지등급 = random.randint(1, 100)
    if 최소데미지등급 <= 1:
        엑스칼리버.최소데미지 = 150
    elif 최소데미지등급 <= 10:
        엑스칼리버.최소데미지 = random.randint(120, 150)
    elif 최소데미지등급 <= 50:
        엑스칼리버.최소데미지 = random.randint(100, 119)
    else:
        엑스칼리버.최소데미지 = random.randint(80, 99)
    if 최대데미지등급 <= 1:
        엑스칼리버.최대데미지 = 250
    elif 최대데미지등급 <= 10:
        엑스칼리버.최대데미지 = random.randint(220, 250)
    elif 최대데미지등급 <= 50:
        엑스칼리버.최대데미지 = random.randint(190, 219)
    else:
        엑스칼리버.최대데미지 = random.randint(160, 189)
    엑스칼리버.초기세팅()
    return 엑스칼리버

def 그리폰():
    그리폰 = 무기('그리폰')
    그리폰.등급 = 6
    그리폰.등급이름 = '신화'
    그리폰.추가능력치['STR'] = 99
    그리폰.추가능력치['DEX'] = 99
    그리폰.무기스킬리스트.append(무기스킬_카무사리())
    최소데미지등급 = random.randint(1, 100)
    최대데미지등급 = random.randint(1, 100)
    if 최소데미지등급 <= 1:
        그리폰.최소데미지 = 259
    elif 최소데미지등급 <= 10:
        그리폰.최소데미지 = random.randint(220, 250)
    elif 최소데미지등급 <= 50:
        그리폰.최소데미지 = random.randint(200, 219)
    else:
        그리폰.최소데미지 = random.randint(180, 199)
    if 최대데미지등급 <= 1:
        그리폰.최대데미지 = 369
    elif 최대데미지등급 <= 10:
        그리폰.최대데미지 = random.randint(320, 350)
    elif 최대데미지등급 <= 50:
        그리폰.최대데미지 = random.randint(290, 319)
    else:
        그리폰.최대데미지 = random.randint(260, 289)
    그리폰.초기세팅()
    return 그리폰

def 에이스():
    에이스 = 무기('에이스')
    에이스.등급 = 6
    에이스.등급이름 = '신화'
    에이스.추가능력치['STR'] = 77
    에이스.추가능력치['DEX'] = 77
    에이스.추가능력치['INT'] = 77
    에이스.추가능력치['CON'] = 77
    에이스.추가능력치['LUK'] = 77
    에이스.무기스킬리스트.append(무기스킬_카무사리())
    데미지등급 = random.randint(1, 100)
    에이스.증폭 = 1.3
    if 데미지등급 <= 5:
        에이스.최소데미지 = 0
        에이스.최대데미지 = 777
    elif 데미지등급 <= 40:
        에이스.최소데미지 = random.randint(100, 150)
        에이스.최대데미지 = random.randint(460, 500)
    elif 데미지등급 <= 80:
        에이스.최소데미지 = random.randint(80, 99)
        에이스.최대데미지 = random.randint(430, 459)
    else:
        에이스.최소데미지 = random.randint(60, 79)
        에이스.최대데미지 = random.randint(400, 429)
    에이스.초기세팅()
    return 에이스

def 혼령의구슬():
    혼령의구슬 = 무기('혼령의 구슬')
    혼령의구슬.등급 = 4
    혼령의구슬.등급이름 = '영웅'
    혼령의구슬.추가능력치['DEX'] = random.randint(3, 5)
    혼령의구슬.추가능력치['INT'] = random.randint(15, 20)
    if random.randint(1, 100) <= 50:
        혼령의구슬.추가능력치['LUK'] = random.randint(3, 6)
    혼령의구슬.무기스킬리스트.append(무기스킬_매혹())
    혼령의구슬.무기스킬리스트.append(무기스킬_요괴화())
    데미지등급 = random.randint(1, 100)
    혼령의구슬.증폭 = 1.2
    if 데미지등급 <= 20:
        혼령의구슬.최소데미지 = 55
        혼령의구슬.최대데미지 = 70
    elif 데미지등급 <= 80:
        혼령의구슬.최소데미지 = random.randint(50, 54)
        혼령의구슬.최대데미지 = random.randint(62, 69)
    else:
        혼령의구슬.최소데미지 = random.randint(45, 49)
        혼령의구슬.최대데미지 = random.randint(56, 61)
    혼령의구슬.초기세팅()
    return 혼령의구슬
