from object.Armor import *

def create_armor(방어구이름):
    if   방어구이름 == '철갑옷': return 제작_철갑옷()
    
    raise(NameError)
