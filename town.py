import os

class Town():
    캐릭터딕셔너리 = {}

    def 저장(캐릭터):
        Town.캐릭터딕셔너리[캐릭터.이름] = 캐릭터

    def 모두저장(캐릭터리스트):
        for 캐릭터 in 캐릭터리스트:
            Town.저장(캐릭터)

    def 불러오기(캐릭터이름):
        return Town.캐릭터딕셔너리[캐릭터이름]

    def 출력():
        for key, value in Town.캐릭터딕셔너리.items():
            value.출력()
