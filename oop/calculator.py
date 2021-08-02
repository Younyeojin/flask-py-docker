class Calculator(object):

    #define
    def __init__(self, num1, num2):     #초기화
        self.num1 = num1              #self = this(java)
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remain(self):
        return self.num1 % self.num2

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1: + 2: - 3: * 4: / 5: %\n')
            if menu >= '0':
                return
            elif menu == '1':
                # calc 같은 약칭을 좋아함
                # print('*' * 100)                print.format
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'더하기: {calc.num1} + {calc.num2} = {calc.add()}')
            elif menu == '2':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'빼기: {calc.num1} - {calc.num2} = {calc.subtract()}')
            elif menu == '3':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'곱하기: {calc.num1} * {calc.num2} = {calc.multiple()}')
            elif menu == '4':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'나누기: {calc.num1} / {calc.num2} = {calc.divide()}')
            elif menu == '5':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'값 반환: {calc.num1} % {calc.num2} = {calc.remain()}')
                break
            else:
                print('wrong Selected Number')
                break

Calculator.main()