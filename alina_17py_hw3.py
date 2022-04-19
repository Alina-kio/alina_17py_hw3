# # #HW:

# # реализовать операцию над дробью, то есть создать класс Fraction у него будет 2 атрибута (numertor, denumerator)
# # сделать add, sub, mul, floordiv (Dunder Methods)
# # по правилам математики!)
# # #ExtraTask:
# # Учитывая целое число x, вернуть, true если x это целое число палиндрома.
# # К сведению: Целое число является палиндромом , если оно читается так же, как в прямом, так и в обратном порядке.
# # Например, 121 есть палиндром, а 123 нет.

class Fraction: 
    def __init__(self, numerator, denominator): 
        self.numerator = numerator 
        self.denominator = denominator 
 
    def __add__(self, other): 
        a = self.numerator + other * self.denominator
        print(f'{other} + ({self.numerator}/{self.denominator}) = {a}/{self.denominator}')
 
    def __sub__(self, other): 
        a = other * self.denominator - self.numerator
        print(f'{other} - ({self.numerator}/{self.denominator}) = {a}/{self.denominator}')
 
    def __mul__(self, other):
        a = self.numerator * other 
        print(f'{other} * ({self.numerator}/{self.denominator}) = {a}/{self.denominator}') 
 
    def __floordiv__(self, other): 
        a = self.numerator // (other  * self.denominator)
        print(f'{other} // ({self.numerator}/{self.denominator}) = {a}/{self.denominator}') 
 
F = Fraction(1, 2)
F.__add__(1/5)
F.__sub__(6)
F.__mul__(6)
F.__floordiv__(6)