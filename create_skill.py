from skill import *

def create_skill(스킬이름):
    if   스킬이름 == '검격':     return 습득_검격()
    elif 스킬이름 == '내려치기': return 무기스킬_내려치기()
    elif 스킬이름 == '시동':     return 무기스킬_시동()
    else:                        raise(NameError)
    