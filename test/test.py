import os

from object.Town                 import 마을
from object.Character            import 캐릭터
from object.Reinforce            import 무기강화
from object.Reinforce            import 갑옷강화
from object.Reinforce            import 장비강화
from object.Reinforce            import 스킬강화
from object.Store                import 상점

from function.dual               import dual
from function.hunt               import hunt
from function.create_character   import test_create_character, create_character
from function.create_monster     import create_monster
from function.create_weapon      import create_weapon
from function.create_armor       import create_armor
from function.create_skill       import create_skill
from function.initial            import initial_loading
from function.create_consumption import create_consumption

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
    마을.출력()
    만패 = 마을.불러오기('만패')
    BIGT0R = 마을.불러오기('BIGT0R')
    만패.출력()
    만패.인벤토리.모두출력()
    #만패.장착_장비(10)
    #만패.저장()

    #주황버섯 = create_monster('주황버섯')
    #주황버섯.출력()
    #산적 = create_monster('산적')
    #산적.출력()
    구미호 = create_monster('구미호')
    구미호.출력()
    hunt(만패, 구미호)
    #만패.장착_장비(3)
    #만패.출력()
    #만패.인벤토리.모두출력()
    #for _ in range(300): 무기강화(만패.무기)
    #만패.무기.출력()
    #만패.저장()
    #팡이 = 마을.불러오기('팡이')
    #dual(만패, 팡이)

    #for _ in range(10): 장비강화(만패.모자)
    #for _ in range(10): 장비강화(만패.갑옷)
    #for _ in range(10): 장비강화(만패.장갑)
    #for _ in range(10): 장비강화(만패.신발)
    #for _ in range(100): 장비강화(만패.코어)

    #만패.해제_장비('모자')
    #만패.해제_장비('갑옷')
    #만패.해제_장비('장갑')
    #만패.해제_장비('신발')
    #만패.해제_장비('코어')
    #만패.해제_무기()
    #만패.장착_장비(1)
    #철투구     = create_armor('철투구')
    #철갑옷     = create_armor('철갑옷')
    #철장갑     = create_armor('철장갑')
    #철신발     = create_armor('철신발')
    #태초의정신 = create_armor('태초의정신')
    #철투구.출력()
    #철갑옷.출력()
    #철장갑.출력()
    #철신발.출력()
    #태초의정신.출력()
    #만패.인벤토리.추가(철투구)
    #만패.인벤토리.추가(철갑옷)
    #만패.인벤토리.추가(철장갑)
    #만패.인벤토리.추가(철신발)
    #만패.인벤토리.추가(태초의정신)
    #만패.인벤토리.모두출력()
    #만패.장착_장비(3)
    #만패.장착_장비(4)
    #만패.장착_장비(5)
    #만패.장착_장비(6)
    #만패.장착_장비(7)
    #만패.출력()
    #만패.인벤토리.모두출력()

    #for _ in range(50): 무기강화(만패.무기)
    #for _ in range(50): 갑옷강화(만패.갑옷)
    #주황버섯 = create_monster('주황버섯')
    #for _ in range(200): hunt(만패, 주황버섯)
    #만패.능력치세팅()
    #만패.출력()
    #만패.인벤토리.모두출력()
    #만패.저장()

    #dual(만패, BIGT0R)
