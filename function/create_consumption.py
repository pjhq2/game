from object.Consumption import *

def create_consumption(소비이름):
    if 소비이름 == '무기강화주문서': return 구매_무기강화주문서()

    raise(NameError)
