from object.Town    import 마을
from object.Monster import *

def create_monster(몬스터이름):
    if   몬스터이름 == '주황버섯': return 몬스터('주황버섯')
    elif 몬스터이름 == '산적'    : return 산적()
    elif 몬스터이름 == '구미호'  : return 구미호()

    raise(NameError)
