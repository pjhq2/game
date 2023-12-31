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
from initial          import initial_loading

import os

def hunt_sequence(불러온캐릭터):
    # 몬스터 사냥
    create_monster('주황버섯')
    주황버섯 = Town.불러오기('주황버섯')
    hunt(불러온캐릭터, 주황버섯)
    # 캐릭터 저장
    불러온캐릭터.저장()

def dual_sequence(캐릭터_1, 캐릭터_2):
    dual(캐릭터_1, 캐릭터_2)

if __name__ == '__main__':
    initial_loading()

    캐릭터이름_1 = '만패'
    캐릭터이름_2 = '팡이'
    # 캐릭터 없으면 생성
    if not os.path.isfile(f'./save/{캐릭터이름_1}.info'):
        만패 = create_character(캐릭터이름_1)
    else:
        만패 = 캐릭터().불러오기(캐릭터이름_1)
    if not os.path.isfile(f'./save/{캐릭터이름_2}.info'):
        사기캐 = create_character(캐릭터이름_2)
    else:
        사기캐 = 캐릭터().불러오기(캐릭터이름_2)

    # 사냥
    hunt_sequence(만패)

    # 듀얼
    dual_sequence(만패, 사기캐)

    # 인벤토리 아이템 없으면 추가
    if 만패.인벤토리.아이템개수() == 0:
        그리폰 = create_weapon('그리폰')
        만패.인벤토리.추가(그리폰)
        참월   = create_weapon('참월')
        만패.인벤토리.추가(참월)
    else:
        print(f'아이템 개수 : {만패.인벤토리.아이템개수()}')        
    
    # 인벤토리 아이템 강화
    무기강화(만패.인벤토리.목록[0])

    # 스킬 강화
    스킬강화(만패.스킬리스트[0])

    # 아이템 스킬 강화
    if len(만패.인벤토리.목록[0].무기스킬리스트) != 0:
        스킬강화(만패.인벤토리.목록[0].무기스킬리스트[0])

    # 인벤토리 아이템 장착
    만패.장착_무기(0)

    # 장착 무기 강화
    무기강화(만패.무기)

    # 상태 출력
    만패.출력()
    만패.인벤토리.모두출력()

    # 캐릭터 저장
    만패.저장()
    사기캐.저장()
