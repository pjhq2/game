from town import Town

from dual             import dual
from create_character import test_create_character
from create_character import create_character
from character        import 캐릭터

if __name__ == '__main__':
    #test_create_character()
    #create_character()
    #캐릭터_1, 캐릭터_2 = Town.캐릭터딕셔너리['99몽둥이'], Town.캐릭터딕셔너리['갓종']
    #dual(캐릭터_1, 캐릭터_2)

    캐릭터이름 = '갓종'
    임시캐릭터 = 캐릭터('임시캐릭터')
    임시캐릭터.불러오기(캐릭터이름)