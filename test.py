from town import Town

from dual             import dual
from hunt             import hunt
from create_character import test_create_character, create_character
from create_monster   import create_monster
from create_weapon    import create_weapon
from create_skill     import create_skill
from character        import 캐릭터
from reinforce        import 무기강화
from reinforce        import 스킬강화

import os

def get_all_character():
    캐릭터파일리스트 = os.listdir('./save')
    캐릭터이름리스트 = []
    캐릭터리스트     = []
    for 캐릭터파일 in 캐릭터파일리스트:
        캐릭터이름리스트.append(캐릭터파일[:-5])
    for 캐릭터이름 in 캐릭터이름리스트:
        캐릭터리스트.append(캐릭터().불러오기(캐릭터이름))
    return 캐릭터리스트

if __name__ == '__main__':
    Town.모두저장(get_all_character())
    동황 = Town.불러오기('동황')
    #Town.출력()
    #동황 = create_character('동황')
    #동황.인벤토리.추가(create_weapon('그리폰'))
    #동황.인벤토리.추가(create_weapon('엑스칼리버'))
    #동황.인벤토리.추가(create_weapon('참월'))
    #동황.인벤토리.추가(create_weapon('글라디우스'))
    #동황.인벤토리.추가(create_weapon('진검'))
    #동황.인벤토리.추가(create_weapon('나무몽둥이'))
    #for _ in range(100): 무기강화(동황.인벤토리.목록[2])
    #for _ in range(100): 무기강화(동황.인벤토리.목록[5])
    #동황.장착_무기(동황.인벤토리.목록[4])
    #del 동황.인벤토리.목록[4]
    동황.출력()
    동황.인벤토리.출력()
    #동황.저장()
    #동황 = Town.불러오기('동황')
    #동황.출력()
    #동황.인벤토리.출력()
    #동황.출력()
    #동황.인벤토리.추가(create_weapon('나무몽둥이'))
    #동황.인벤토리.추가(create_weapon('진검'))
    #동황.출력()
    #동황.저장()
    #test_create_character()
    #create_character()
    #캐릭터_1, 캐릭터_2 = Town.캐릭터딕셔너리['99몽둥이'], Town.캐릭터딕셔너리['갓종']
    #dual(캐릭터_1, 캐릭터_2)

    #캐릭터이름 = '99몽둥이'
    #임시캐릭터 = 캐릭터('임시캐릭터').불러오기(캐릭터이름)
    #임시캐릭터.출력()
#
    #캐릭터이름 = '사기캐'
    #내캐릭터 = 캐릭터('임시캐릭터').불러오기(캐릭터이름)
    #내캐릭터.출력()

    #dual(임시캐릭터, 내캐릭터)
    #엑칼 = create_weapon('엑스칼리버')
    #내캐릭터.장착_무기(엑칼)
    #내캐릭터.출력()
    #내캐릭터.저장()
    #for _ in range(1): 무기강화(내캐릭터.무기)
    #내캐릭터.출력()
    #내캐릭터.저장()
    #엑스칼리버 = create_weapon('엑스칼리버')
    #엑스칼리버.출력()
    #내캐릭터.장착_무기(엑스칼리버)
    #내캐릭터.출력()
    #내캐릭터.저장()
    #주황버섯 = create_monster('주황버섯')
    #for _ in range(100): hunt(내캐릭터, 주황버섯)
    #내캐릭터.출력()
    #내캐릭터.저장()
    #for _ in range(100): 무기강화(내캐릭터.무기)
    #for _ in range(30):
    #    for i, 스킬 in enumerate(내캐릭터.스킬리스트):
    #        내캐릭터.스킬리스트[i] = 스킬강화(스킬)
    #for _ in range(100):
    #    for i, 무기스킬 in enumerate(내캐릭터.무기.무기스킬리스트):
    #        스킬강화(무기스킬)
    #내캐릭터.저장()
    #내캐릭터.출력()
    # 캐릭터 저장
    #내캐릭터.저장()
    #내캐릭터.출력()
