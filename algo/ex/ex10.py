class MathMethod:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def decrease(self):
        if self.a > self.b:
            return self.a * self.b
        else:
            return self.b - self.a


math = MathMethod(10,5)
print(math.add(), math.decrease())

