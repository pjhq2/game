import os

from object.Town               import 마을
from object.Character          import 캐릭터
from object.Reinforce          import 무기강화
from object.Reinforce          import 스킬강화

from function.dual             import dual
from function.hunt             import hunt
from function.create_character import test_create_character, create_character
from function.create_monster   import create_monster
from function.create_weapon    import create_weapon
from function.create_skill     import create_skill
from function.initial          import initial_loading

def get_all_character():
    캐릭터파일리스트 = os.listdir('./save')
    캐릭터이름리스트 = []
    캐릭터리스트     = []
    for 캐릭터파일 in 캐릭터파일리스트:
        캐릭터이름리스트.append(캐릭터파일[:-5])
    for 캐릭터이름 in 캐릭터이름리스트:
        캐릭터리스트.append(캐릭터().불러오기(캐릭터이름))
    return 캐릭터리스트

def test():
    initial_loading()

    만패 = 마을.불러오기('만패')
    만패.출력()
    만패.인벤토리.모두출력()

    만패.직업 = '도적'

    진검 = create_weapon('진검')
    만패.인벤토리.추가(진검)
    만패.인벤토리.모두출력()

    만패.장착_장비(0)
    만패.인벤토리.모두출력()
    만패.출력()

    for _ in range(200): 무기강화(만패.무기)
    if len(만패.무기.무기스킬리스트) != 0:
        for _ in range(120): 스킬강화(만패.무기.무기스킬리스트[0])
    만패.무기.출력()

    주황버섯 = create_monster('주황버섯')
    for _ in range(100): hunt(만패, 주황버섯)
    만패.저장()

    팡이 = 마을.불러오기('팡이')
    dual(만패, 팡이)
