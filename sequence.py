from town             import Town

from create_character import create_character, test_create_character
from create_weapon    import create_weapon
from create_skill     import create_skill
from create_monster   import create_monster
from dual             import dual
from hunt             import hunt
from character        import 캐릭터

import os, time

def basic_sequence():
    # 캐릭터 생성 & 무기/스킬 장착 & 저장
    만패       = create_character('만패')
    나무몽둥이 = create_weapon('나무몽둥이')
    검격       = create_skill('검격')
    만패.장착_무기(나무몽둥이)
    만패.스킬리스트.append(검격)
    Town.캐릭터딕셔너리['만패'] = 만패
    만패.저장()
    # 몬스터 생성
    주황버섯 = create_monster('주황버섯')
    # 몬스터 사냥 10회
    for _ in range(1): hunt(만패, 주황버섯)
    # 캐릭터 저장
    만패.저장()

def load_sequence(닉네임):
    # 캐릭터 불러오기
    불러온캐릭터 = 캐릭터('불러온캐릭터').불러오기(닉네임)
    # 몬스터 사냥 10회
    create_monster('주황버섯')
    주황버섯 = Town.캐릭터딕셔너리['주황버섯']
    for _ in range(10): hunt(불러온캐릭터, 주황버섯)
    # 캐릭터 저장
    불러온캐릭터.저장()
    불러온캐릭터.출력()
    

if __name__ == '__main__':
    #test_create_character()
    #캐릭터_1, 캐릭터_2 = Town.캐릭터딕셔너리['성레기'], Town.캐릭터딕셔너리['갓종']
    #dual(캐릭터_1, 캐릭터_2)
    캐릭터이름 = '만패'
    if not os.path.isfile(f'./save/{캐릭터이름}.info'):
        basic_sequence()
    load_sequence(캐릭터이름)
    