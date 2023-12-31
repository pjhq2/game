class 인벤토리():
    def __init__(self):
        self.목록 = []

    def 추가(self, 아이템):
        self.목록.append(아이템)
        return self

    def 제거(self, 아이템):
        for item in self.목록:
            if item.id == 아이템.id:
                self.목록.delete(item)
                break
        return self
    
    def 출력(self):
        for 아이템 in self.목록:
            아이템.출력()
