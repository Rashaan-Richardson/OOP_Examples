import logging
import math

# Logging statment. "basic config(filename = path /what you want to call your logger",level = logging level)
logging.basicConfig(filename='/Users/rashaanrichardson/Desktop/PY_121_Class/Basic_Math_Logger',level=logging.INFO)

class Numbers:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add_num(self):
        logging.info(f'The sum of these numbers is {self.num1 + self.num2}')

    def sub_num(self):
        logging.info(f'The two numbers subtracted equals {self.num1 - self.num2}')

    def multi(self):
        logging.info(f'The product of these numbers is {self.num1 * self.num2}')

    def divide(self):
        logging.info(f'The result of the division is {self.num1/self.num2}')

    def findPrime(self):
        if(self.num1 > 1):
            prime = True
            for i in range(2, int(math.sqrt(self.num1) + 1)):
                if self.num1 % i == 0:
                    prime = False
                    break
        logging.info('Prime' if prime else 'Composite')

if  __name__ == '__main__':
    
    num_operations = Numbers(3,4)
    num_operations.add_num()
    num_operations.sub_num()
    num_operations.multi()
    num_operations.divide()
    num_operations.findPrime()
