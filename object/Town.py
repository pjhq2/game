class 마을():
    캐릭터딕셔너리 = {}

    def 저장(캐릭터):
        마을.캐릭터딕셔너리[캐릭터.이름] = 캐릭터

    def 모두저장(캐릭터리스트):
        for 캐릭터 in 캐릭터리스트:
            마을.저장(캐릭터)

    def 불러오기(캐릭터이름):
        return 마을.캐릭터딕셔너리[캐릭터이름]

    def 출력():
        print('========== 마을 ==========')
        for 캐릭터 in 마을.캐릭터딕셔너리.values():
            print(f' {캐릭터.이름} Lv.{캐릭터.레벨}')
        print('==========================')