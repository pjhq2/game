from system.object.Armor import *

def create_armor(방어구이름):
    if   방어구이름 == '철투구': return 철투구()
    elif 방어구이름 == '철갑옷': return 철갑옷()
    elif 방어구이름 == '철장갑': return 철장갑()
    elif 방어구이름 == '철신발': return 철신발()
    elif 방어구이름 == '태초의정신': return 태초의정신()
    
    raise(NameError)
