from system.object.Consumption import *

def create_consumption(소비이름):
    if   소비이름 == '무기강화주문서':   return 무기강화주문서()
    elif 소비이름 == '방어구강화주문서': return 방어구강화주문서()

    raise(NameError)
