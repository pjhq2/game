from Item import 소비아이템

class 물약(소비아이템):
    def __init__(self, 이름):
        super().__init__(이름)

class 주문서(소비아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        