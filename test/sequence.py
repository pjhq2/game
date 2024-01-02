import os

from master                    import gprint

from object.Town               import 마을
from object.Character          import 캐릭터
from object.Reinforce          import 무기강화
from object.Reinforce          import 갑옷강화
from object.Reinforce          import 스킬강화
from object.Store              import 상점

from function.initial          import initial_loading
from function.create_character import create_character, test_create_character
from function.create_weapon    import create_weapon
from function.create_armor     import create_armor
from function.create_skill     import create_skill
from function.create_monster   import create_monster
from function.dual             import dual
from function.hunt             import hunt

def character_file_sequence(캐릭터이름):
    # 캐릭터 없으면 생성
    if not os.path.isfile(f'./save/{캐릭터이름}.info'):
        내캐릭터 = create_character(캐릭터이름)
    # 캐릭터 있으면 불러오기
    else:
        내캐릭터 = 캐릭터().불러오기(캐릭터이름)
    return 내캐릭터

def character_town_sequence(캐릭터이름):
    return 마을.불러오기(캐릭터이름)

def hunt_sequence(불러온캐릭터):
    # 몬스터 사냥
    주황버섯 = create_monster('주황버섯')
    hunt(불러온캐릭터, 주황버섯)
    # 캐릭터 저장
    불러온캐릭터.저장()

def dual_sequence(캐릭터_1, 캐릭터_2):
    dual(캐릭터_1, 캐릭터_2)

def sequence():
    # 마을에 모든 캐릭터 로딩
    print('########## 마을에 모든 캐릭터 로딩 ##########')
    initial_loading()

    # 파일에서 캐릭터 불러오기
    print('########## 파일에서 캐릭터 불러오기 ##########')
    만패       = character_file_sequence('만패')
    BIGT0R     = character_file_sequence('BIGT0R')

    # 마을에서 캐릭터 가져오기
    #print('########## 마을에서 캐릭터 가져오기 ##########')
    #만패   = character_town_sequence('만패')
    #BIGT0R = character_town_sequence('BIGT0R')

    # 인벤토리 아이템 없으면 추가
    print('########## 인벤토리 아이템 없으면 추가 ##########')
    if 만패.인벤토리.아이템개수() == 0:
        엑스칼리버 = create_weapon('엑스칼리버')
        만패.인벤토리.추가(엑스칼리버)
        참월   = create_weapon('참월')
        만패.인벤토리.추가(참월)
        에이스 = create_weapon('에이스')
        만패.인벤토리.추가(에이스)
        철갑옷 = create_armor('철갑옷')
        만패.인벤토리.추가(철갑옷)
    
    # 인벤토리 아이템 강화
    print('########## 인벤토리 아이템 강화 ##########')
    인벤토리인덱스 = 0
    if 만패.인벤토리.목록[인벤토리인덱스] != None and 만패.인벤토리.목록[인벤토리인덱스].유형 == '무기':
        for _ in range(3): 무기강화(만패.인벤토리.목록[인벤토리인덱스])

    # 스킬 강화
    print('########## 스킬 강화 ##########')
    스킬인덱스 = 0
    if len(만패.스킬리스트) != 0:
        for _ in range(3): 스킬강화(만패.스킬리스트[스킬인덱스])

    # 아이템 스킬 강화
    print('########## 아이템 스킬 강화 ##########')
    인벤토리인덱스 = 0
    무기스킬인덱스 = 0
    if 만패.인벤토리.목록[인벤토리인덱스] != None and 만패.인벤토리.목록[인벤토리인덱스].유형 == '무기':
        if len(만패.인벤토리.목록[인벤토리인덱스].무기스킬리스트) != 0:
            for _ in range(3): 스킬강화(만패.인벤토리.목록[인벤토리인덱스].무기스킬리스트[무기스킬인덱스])

    # 인벤토리 아이템 장착
    print('########## 인벤토리 아이템 장착 ##########')
    인벤토리인덱스 = 2
    만패.장착_장비(인벤토리인덱스)  # 에이스
    인벤토리인덱스 = 3
    만패.장착_장비(인벤토리인덱스)  # 철갑옷

    # 장착 장비 강화
    print('########## 장착 장비 강화 ##########')
    for _ in range(5): 무기강화(만패.무기)
    for _ in range(5): 갑옷강화(만패.갑옷)

    # 상점 구매 / 판매
    print('########## 상점 구매 / 판매 ##########')
    주문서상점 = 상점('주문서상점')
    주문서상점.출력()
    무기강화주문서   = 주문서상점.목록[0]
    방어구강화주문서 = 주문서상점.목록[1]
    무기강화주문서인덱스   = 만패.아이템구매(무기강화주문서,   3)
    방어구강화주문서인덱스 = 만패.아이템구매(방어구강화주문서, 3)
    만패.아이템판매(무기강화주문서인덱스,   1)
    만패.아이템판매(방어구강화주문서인덱스, 2)
    만패.인벤토리.모두출력()

    # 아이템 찾기 & 이동
    print('########## 아이쳄 찾기 & 이동 ##########')
    인덱스, 아이템 = 만패.인벤토리.이름으로찾기('방어구강화주문서')
    만패.인벤토리.이동(인덱스, 20)
    만패.인벤토리.이동(20, 0)

    # 무기 강화 (무기강화주문서 사용)
    print('########## 무기 강화 (무기강화주문서 사용) ##########')
    인덱스, 아이템 = 만패.인벤토리.이름으로찾기('무기강화주문서')
    if 아이템:
        if 아이템.개수 == 1:  만패.인벤토리.제거(인덱스)
        elif 아이템.개수 > 1: 아이템.개수 -= 1
        else:                 raise(ValueError)
        무기강화(만패.무기)
        만패.인벤토리.모두출력()

    # 장착무기 스킬 강화
    print('########## 장착무기 스킬 강화 ##########')
    if len(만패.무기.무기스킬리스트) != 0:
        무기스킬인덱스 = 0
        스킬강화(만패.무기.무기스킬리스트[무기스킬인덱스])
    
    # 사냥
    print('########## 사냥 ##########')
    for _ in range(1): hunt_sequence(만패)

    # 듀얼
    print('########## 듀얼 ##########')
    dual_sequence(만패, BIGT0R)

    # 상태 출력
    print('########## 상태 출력 ##########')
    만패.출력()
    만패.인벤토리.모두출력()

    # 캐릭터 저장
    print('########## 캐릭터 저장 ##########')
    만패.저장()
    BIGT0R.저장()
