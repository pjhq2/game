from weapon import *

def create_weapon(무기이름):
    if   무기이름 == '나무몽둥이': return 제작_나무몽둥이()
    elif 무기이름 == '진검':       return 제작_진검()
    elif 무기이름 == '글라디우스': return 제작_글라디우스()
    elif 무기이름 == '참월':       return 제작_참월()
    elif 무기이름 == '엑스칼리버': return 제작_엑스칼리버()
    elif 무기이름 == '그리폰':     return 제작_그리폰()
    else:                          raise(NameError)
