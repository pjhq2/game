import os

from system.object.Town                 import 마을
from system.object.Character            import 캐릭터
from system.object.Reinforce            import 무기강화
from system.object.Reinforce            import 갑옷강화
from system.object.Reinforce            import 장비강화
from system.object.Reinforce            import 스킬강화
from system.object.Store                import 상점

from system.function.dual               import dual
from system.function.hunt               import hunt
from system.function.create_character   import test_create_character, create_character
from system.function.create_monster     import create_monster
from system.function.create_weapon      import create_weapon
from system.function.create_armor       import create_armor
from system.function.create_skill       import create_skill
from system.function.initial            import initial_loading
from system.function.create_consumption import create_consumption

def get_all_character():
    캐릭터파일리스트 = os.listdir(os.getenv('SAVE_DIR'))
    캐릭터이름리스트 = []
    캐릭터리스트     = []
    for 캐릭터파일 in 캐릭터파일리스트:
        캐릭터이름리스트.append(캐릭터파일[:-5])
    for 캐릭터이름 in 캐릭터이름리스트:
        캐릭터리스트.append(캐릭터().불러오기(캐릭터이름))
    return 캐릭터리스트

def test():
    initial_loading()
    루피 = create_character('루피')
    루피.출력()

    주문서상점 = 상점('주문서상점')
    주문서상점.출력()
    무기강화주문서   = 주문서상점.목록[0]
    방어구강화주문서 = 주문서상점.목록[1]
    무기강화주문서인덱스   = 루피.아이템구매(무기강화주문서,   76)
    방어구강화주문서인덱스 = 루피.아이템구매(방어구강화주문서, 88)
    루피.인벤토리.모두출력()

    철투구     = create_armor('철투구')
    철갑옷     = create_armor('철갑옷')
    철장갑     = create_armor('철장갑')
    철신발     = create_armor('철신발')
    태초의정신 = create_armor('태초의정신')
    나무몽둥이 = create_weapon('나무몽둥이')
    진검 = create_weapon('진검')
    글라디우스 = create_weapon('글라디우스')
    참월 = create_weapon('참월')
    그리폰 = create_weapon('그리폰')
    에이스 = create_weapon('에이스')
    혼령의구슬 = create_weapon('혼령의 구슬')
    루피.인벤토리.추가(철투구)
    루피.인벤토리.추가(철갑옷)
    루피.인벤토리.추가(철장갑)
    루피.인벤토리.추가(철신발)
    루피.인벤토리.추가(태초의정신)
    루피.인벤토리.추가(나무몽둥이)
    루피.인벤토리.추가(진검)
    루피.인벤토리.추가(글라디우스)
    루피.인벤토리.추가(참월)
    루피.인벤토리.추가(그리폰)
    루피.인벤토리.추가(에이스)
    루피.인벤토리.추가(혼령의구슬)
    루피.인벤토리.모두출력()
    루피.장착_장비(2)
    루피.장착_장비(3)
    루피.장착_장비(4)
    루피.장착_장비(5)
    루피.장착_장비(6)
    루피.장착_장비(13)
    루피.인벤토리.추가(철투구)
    루피.인벤토리.추가(철갑옷)
    루피.인벤토리.추가(철장갑)
    루피.인벤토리.추가(철신발)
    루피.인벤토리.추가(태초의정신)
    루피.인벤토리.추가(나무몽둥이)
    루피.인벤토리.추가(진검)
    루피.인벤토리.추가(글라디우스)
    루피.인벤토리.추가(참월)
    루피.인벤토리.추가(그리폰)
    루피.인벤토리.추가(에이스)
    루피.인벤토리.추가(혼령의구슬)
    루피.출력()
    루피.인벤토리.모두출력()

    만패 = 마을.불러오기('만패')
    dual(만패, 루피)
