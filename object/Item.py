import time

class 아이템():
    def __init__(self, 이름):
        self.id             = hex(int(''.join(str(time.time()).split('.'))))[2:]  # hex string
        self.이름           = 이름
        self.등급           = 1
        self.등급이름       = '일반'

class 장비아이템(아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.강화레벨       = 0
        self.최고강화레벨   = 100

class 소비아이템(아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.개수 = 0

class 기타아이템(아이템):
    def __init__(self, 이름):
        super().__init__(이름)
        self.개수 = 0
