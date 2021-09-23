import math

class Numbers:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add_num(self):
        return f'The sum of these numbers is {self.num1 + self.num2}'

    def sub_num(self):
        return f'The two numbers subtracted equals {self.num1 - self.num2}'

    def multi(self):
        return f'The product of these numbers is {self.num1 * self.num2}'

    def divide(self):
        return f'The result of the division is {self.num1/self.num2}'

    def findPrime(self, num):
        if(num > 1):
            prime = True
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    prime = False
                    break
        return 'Prime' if prime else 'Composite'

if  __name__ == '__main__':
    num_operations = Numbers(3,4)
    print(num_operations.add_num())
    print(num_operations.sub_num())
    print(num_operations.multi())
    print(num_operations.divide())