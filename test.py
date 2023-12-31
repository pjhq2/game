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
from initial          import initial_loading

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
    initial_loading()

    만패 = Town.불러오기('만패')
    만패.출력()
    만패.인벤토리.모두출력()

    #만패.직업 = '도적'

    #진검 = create_weapon('진검')
    #만패.인벤토리.추가(진검)
    #만패.인벤토리.모두출력()

    #만패.장착_무기(0)
    #만패.인벤토리.모두출력()
    #만패.출력()

    #for _ in range(200): 무기강화(만패.무기)
    #for _ in range(120): 스킬강화(만패.무기.무기스킬리스트[0])
    #만패.무기.출력()

    #주황버섯 = create_monster('주황버섯')
    #for _ in range(100): hunt(만패, 주황버섯)
    #만패.저장()

    팡이 = Town.불러오기('팡이')
    팡이.회피 = 10.0
    dual(만패, 팡이)
