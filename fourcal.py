# class Cal:
#     def __init__(self, num1):
#         self._num1 = num1
#         self._result = num1
#     def add(self, num2):
#         self._result += num2
#         return self._result
#
#     def sub(self, num2):
#         self._result -= num2
#         return self._result
#
#     def mul(self, num2):
#         self._result *= num2
#         return self._result
#
#     def div(self, num2):
#         self._result /= num2
#         return self._result

class Calculator:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self._result = 0
    def add(self):
        self._result = self._num1 + self._num2  #그냥 num1,2로 하면 안 되는 듯? (self, num1, num2)이런 식으로 돼 있을 때 되는 듯
        return self._result

    def sub(self):
        self._result = self._num1 - self._num2
        return self._result

    def mul(self):
        self._result = self._num1 * self._num2
        return self._result

    def div(self):
        self._result = self._num1 / self._num2
        return self._result

# ex = Calculator(10, 5)
# print(ex.add())
# print(ex.sub())
# print(ex.mul())
# print(ex.div())