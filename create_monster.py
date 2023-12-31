from town import Town

from monster import *

def create_monster(몬스터이름):
    생성몬스터 = 몬스터(몬스터이름)
    Town.저장(생성몬스터)
    return 생성몬스터
