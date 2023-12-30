from town      import Town

from character import 캐릭터
from weapon    import 제작_엑스칼리버
from weapon    import 제작_진검
from weapon    import 제작_나무몽둥이
from skill     import 습득_검격

def test_create_character():
    for i in range(1000):
        테스트캐릭터 = 캐릭터(f'테스트{i:03d}')
        테스트캐릭터.출력()
        테스트캐릭터.저장()
    for key, value in Town.캐릭터딕셔너리.items():
        print(f'{key} - {value}')

def create_character(닉네임):
    생성캐릭터 = 캐릭터(닉네임)
    생성캐릭터.처음생성()
    생성캐릭터.출력()
    생성캐릭터.저장()
    return 생성캐릭터

def test_create_character():
    캐릭터_1 = 캐릭터('성레기')
    캐릭터_1.장착_무기(제작_엑스칼리버())
    for _ in range(10): 캐릭터_1.무기.강화레벨업()
    #캐릭터_1.무기.출력()
    캐릭터_1.직업 = '도적'
    for _ in range(32): 캐릭터_1.레벨업()
    #캐릭터_1.출력()
    캐릭터_1.저장()

    캐릭터_2 = 캐릭터('갓종')
    캐릭터_2.장착_무기(제작_진검())
    for _ in range(50): 캐릭터_2.무기.강화레벨업()
    #캐릭터_2.무기.출력()
    캐릭터_2.직업 = '전사'
    for _ in range(99): 캐릭터_2.레벨업()
    캐릭터_2.스킬리스트.append(습득_검격())
    #캐릭터_2.출력()
    캐릭터_2.저장()

    캐릭터_3 = 캐릭터('99몽둥이')
    캐릭터_3.장착_무기(제작_나무몽둥이())
    for _ in range(99): 캐릭터_3.무기.강화레벨업()
    #캐릭터_3.무기.출력()
    캐릭터_3.직업 = '초보자'
    for _ in range(0): 캐릭터_3.레벨업()
    #캐릭터_3.출력()
    캐릭터_3.저장()

if __name__ == '__main__':
    test_create_character()
    