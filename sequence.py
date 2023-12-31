from town             import Town

from create_character import create_character, test_create_character
from create_weapon    import create_weapon
from create_skill     import create_skill
from create_monster   import create_monster
from dual             import dual
from hunt             import hunt
from character        import 캐릭터
from reinforce        import 무기강화
from reinforce        import 스킬강화

import os, time

def basic_sequence(닉네임):
    # 캐릭터 생성 & 무기/스킬 장착 & 저장
    내캐릭터   = create_character(닉네임)
    나무몽둥이 = create_weapon('나무몽둥이')
    검격       = create_skill('검격')
    내캐릭터.장착_무기(나무몽둥이)
    내캐릭터.스킬리스트.append(검격)
    Town.캐릭터딕셔너리[닉네임] = 내캐릭터
    내캐릭터.저장()
    # 몬스터 생성
    주황버섯 = create_monster('주황버섯')
    # 몬스터 사냥 10회
    for _ in range(1): hunt(내캐릭터, 주황버섯)
    # 캐릭터 저장
    내캐릭터.저장()

def hunt_sequence(닉네임):
    # 캐릭터 불러오기
    불러온캐릭터 = 캐릭터('불러온캐릭터').불러오기(닉네임)
    # 몬스터 사냥 10회
    create_monster('주황버섯')
    주황버섯 = Town.캐릭터딕셔너리['주황버섯']
    for _ in range(10): hunt(불러온캐릭터, 주황버섯)
    # 무기 강화 10회
    for _ in range(10): 무기강화(불러온캐릭터.무기)
    # 스킬 강화 3회
    for _ in range(3):
        for i, 스킬 in enumerate(불러온캐릭터.스킬리스트):
            불러온캐릭터.스킬리스트[i] = 스킬강화(스킬)
    # 캐릭터 저장
    불러온캐릭터.저장()

def dual_sequence(닉네임_1, 닉네임_2):
    # 캐릭터_1, 캐릭터_2 불러오기
    캐릭터_1 = 캐릭터('캐릭터_1').불러오기(닉네임_1)
    캐릭터_2 = 캐릭터('캐릭터_2').불러오기(닉네임_2)
    dual(캐릭터_1, 캐릭터_2)

if __name__ == '__main__':
    캐릭터이름_1 = '만패'
    캐릭터이름_2 = '사기캐'
    # 캐릭터 없으면 생성
    if not os.path.isfile(f'./save/{캐릭터이름_1}.info'):
        basic_sequence(캐릭터이름_1)
    if not os.path.isfile(f'./save/{캐릭터이름_2}.info'):
        basic_sequence(캐릭터이름_2)
    # 사냥
    hunt_sequence(캐릭터이름_1)
    # 듀얼
    dual_sequence(캐릭터이름_1, 캐릭터이름_2)
    