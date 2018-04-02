class Fraction1:

    def __init__(self,numerator,denominator):
        assert((denominator!=0))
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    # def display(self):
    #     print(str(self.numerator)+"/"+str(self.denominator))

    def add(self,that):
        return (Fraction1((self.numerator * that.denominator + self.denominator * that.numerator),(self.denominator * that.denominator)))


    def __add__(self, that):
        return (Fraction1((self.numerator * that.denominator + self.denominator * that.numerator),(self.denominator * that.denominator)))

    def __sub__(self, that):
        return (Fraction1((self.numerator * that.denominator - self.denominator * that.numerator),(self.denominator * that.denominator)))

    def __mul__(self, that):
        return (Fraction1((self.numerator * that.denominator * self.denominator * that.numerator),(self.denominator * that.denominator)))

    def toDecimal(self):
        return self.numerator/self.denominator

f1 = Fraction1(1,2)
f2= Fraction1(2,3)

print(f1+f2)
print(f1-f2)
print(f1 * f2)
print(f1.toDecimal())