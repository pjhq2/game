import random

class 스킬():
    def __init__(self, 이름='강타'):
        self.이름     = 이름
        self.레벨     = 1
        self.등급     = 1
        self.데미지   = 0
        self.유형     = '액티브'
        self.지속시간 = 1
        self.증폭     = 1.0
        self.최고레벨 = 5 + self.등급*5

    def 스킬레벨업(self):
        self.레벨 += 1
        self.데미지 += self.등급*4
        self.증폭   += (self.등급+5)/100

def 습득_검격():
    검격 = 스킬('검격')
    검격.등급     = 2
    검격.데미지   = 15
    검격.증폭     = 1.1
    검격.최고레벨 = 5 + 검격.등급*5
    return 검격

def 무기스킬_내려치기():
    내려치기 = 스킬('내려치기')
    내려치기.데미지   = 8
    내려치기.증폭     = 1.05
    내려치기.최고레벨 = 5 + 내려치기.등급*5
    return 내려치기

def 무기스킬_월아천충():
    월아천충 = 스킬('월아천충')
    월아천충.등급     = 4
    월아천충.데미지   = 60
    월아천충.증폭     = 1.3
    월아천충.지속시간 = 1
    월아천충.최고레벨 = 5 + 월아천충.등급*5
    return 월아천충

def 무기스킬_시동():
    시동 = 스킬('시동')
    시동.등급     = 5
    시동.데미지   = 100
    시동.증폭     = 10
    시동.지속시간 = 2
    시동.최고레벨 = 5 + 시동.등급*5
    return 시동

def 무기스킬_카무사리():
    카무사리 = 스킬('카무사리')
    카무사리.등급     = 6
    카무사리.데미지   = 999
    카무사리.증폭     = 99
    카무사리.지속시간 = 1
    카무사리.최고레벨 = 5 + 카무사리.등급*5
    return 카무사리
