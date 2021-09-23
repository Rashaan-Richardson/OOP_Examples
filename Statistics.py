import math

class Basic_Stat:
    # The constructor
    def __init__(self,lst):
        self.lst = lst

    def calc_mean(self):
        return sum(self.lst)/len(self.lst)

    def calc_median(self):
        if len(self.lst) % 2 == 0:
            pos = (len(self.lst)/2) - 1
            median = (self.lst.sort()[int(pos+1)] + self.lst.sort()[int(pos)])/2
        else:
            median = self.lst.sort()[int(((len(self.lst) + 1)/2) - 1)]

    def calc_max(self):
        return max(self.lst)

    def calc_min(self):
        return min(self.lst)

    def calc_range(self):
        return max(self.lst) - min(self.lst)
    
    def calc_variance(self):
        mean = sum(self.lst)/len(self.lst) #step 1 - Calculate the mean
        sq = 0
        for i in self.lst:
            x = i - mean   #step 2 - Subtract the mean from each number
            s = x ** 2     #step 3 - Square the difference of each value
            sq += s        #step 4 - Sum the squares
        return sq/len(self.lst)  #  step 5 - Divide by the number of items

    def calc_sd(self):
        return math.sqrt(self.calc_variance())  

    def range(self):
        return range(self.lst)
