"""
Реализовать класс - аналог Range
"""


class Iteration:
    def __init__(self,start=0, finish=0, step=1):
        self.start=start
        self.finish=finish
        self.step=step

    def __iter__(self):
        self.current=self.start
        return self

#in case when user try to use next method, but the range limit is over, he get none value

    def __next__(self):
        if self.current<self.finish:
            value=self.current
            self.current+=self.step
            return value
        else:
            pass

a=Iteration(2,2,2)
i=iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


#same values using range:

for l in range(4,9,2):
    print(f'{l}')