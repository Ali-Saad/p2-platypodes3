class Factorial:

    def work(n):
        i = 0
        list = []
        while i != n:
            list.append(n-i)
            i = i + 1
        print(*list, sep = " * ")
    work(8)

    def fact1(self, n):
        self._fact1=fact1
        if n == 0:
            return 1
        else:
            return n * self.fact1(n - 1)
f = Factorial()
print("=", f.fact1(8))

@property
def get_fact1(self):
    return self.fact1

## make sure to change your input on lines 10 and 18 for the work() and fact() 
