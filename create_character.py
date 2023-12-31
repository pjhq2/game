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

if __name__ == '__main__':
    create_character('동황')
    