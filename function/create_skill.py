from object.Skill import *

def create_skill(스킬이름):
    # 캐릭터 스킬
    if   스킬이름 == '검격':     return 습득_검격()
    # 무기 스킬
    if   스킬이름 == '내려치기': return 무기스킬_내려치기()
    elif 스킬이름 == '월아천충': return 무기스킬_월아천충()
    elif 스킬이름 == '시동':     return 무기스킬_시동()
    elif 스킬이름 == '카무사리': return 무기스킬_카무사리()
    
    raise(NameError)
    