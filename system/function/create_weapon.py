from object.Weapon      import *

def create_weapon(무기이름):
    if   무기이름 == '나무몽둥이':  return 나무몽둥이()
    elif 무기이름 == '진검':        return 진검()
    elif 무기이름 == '글라디우스':  return 글라디우스()
    elif 무기이름 == '참월':        return 참월()
    elif 무기이름 == '엑스칼리버':  return 엑스칼리버()
    elif 무기이름 == '그리폰':      return 그리폰()
    elif 무기이름 == '에이스':      return 에이스()
    elif 무기이름 == '혼령의 구슬': return 혼령의구슬()
    
    raise(NameError)
