from .Item import 소비아이템

class 소비(소비아이템):
    def __init__(self, 이름, 유형):
        super().__init__(이름)
        self.유형 = 유형

    def 출력(self):
        print(self.이름)

def 무기강화주문서():
    무기강화주문서 = 소비('무기강화주문서', '주문서')
    return 무기강화주문서

def 방어구강화주문서():
    방어구강화주문서 = 소비('방어구강화주문서', '주문서')
    return 방어구강화주문서
