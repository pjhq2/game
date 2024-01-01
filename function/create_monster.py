from object.Town    import 마을
from object.Monster import 몬스터

def create_monster(몬스터이름):
    생성몬스터 = 몬스터(몬스터이름)
    마을.저장(생성몬스터)
    return 생성몬스터
