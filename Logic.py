#November 1st 2021

class Operator(object):
    def __init__(self, val1, val2 = 0):
        self.val1 = val1
        self.val2 = val2

    def operation_xor(self):
        return self.val1 ^ self.val2

    def operation_or(self):
        return self.val1 | self.val2

    def operation_and(self):
        return self.val1 & self.val2

    def operation_not(self):
        return ~self.val1


#demonstrating use

print(Operator(10,20).operation_xor())
print(Operator(10,20).operation_or())
print(Operator(10,20).operation_and())
print(Operator(10).operation_not())

