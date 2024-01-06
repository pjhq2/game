from .Consumption import 무기강화주문서
from .Consumption import 방어구강화주문서

class 상점():
    def __init__(self, 이름):
        self.이름 = 이름
        self.목록 = []
        self.세팅_목록()
    
    def 세팅_목록(self):
        if self.이름 == '주문서상점':
            self.목록.append(무기강화주문서())
            self.목록.append(방어구강화주문서())

    def 출력(self):
        print(f'========== 상점 ==========')
        for 인덱스, 아이템 in enumerate(self.목록):
            print(f'[{인덱스}] {아이템.이름}')
        print(f'==========================')
        