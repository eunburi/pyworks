class Caulculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y
    """
    if self.y == 0:
        return 0 #0으로 종료
    else:
        return self.x /self.y
    
    """

    try:
        return self.x / self.y
    except ZeroDivisionError as e:
        #retun "0으로 나눌수 없습니다."
        return e

    cal1 = M