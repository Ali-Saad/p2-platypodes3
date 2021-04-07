class Factorial:
    # need the init
    def __init__(self, input):
        # init the vairables
        self._input = input
        self._list = []
        self._string = ''
        # init the helper functions (objects)
        # self.fact1(n)

        self.FactorialCalc()
        #self.Document()

    # helper function
    def FactorialCalc(self):

        # this factorial system works
        n = self._input
        fact = 1

        for i in range(1,n+1):
            fact = fact * i

        i = 0
        string = self._string
        list = []
        while i != n:
            list.append(n-i)
            string = string + str(n-i)
            string = string + "*"
            i = i + 1

        self._string = string
        self._input = fact

    @property
    def output(self):
        return self._input
        # getters, what is passed to the front end to display

        # @property
        # def get_fact1(self):
        #     return self.fact1

    @property
    def work(self):
        return self._string

# f = Factorial()
# print("=", f.fact1(5))



if __name__ == "__main__":
    # getting the user input
    while True:
        try:
            # asks user for an integer value
            n = int(input('Enter a number to find its factorial: '))
            # if user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
            if n > 1000000 or n < 0:
                raise ValueError
            break
        # ValueError sends an error message
        except ValueError:
            print('Invalid value or value too large. Value must be between 0 and 1 000 000. Please try again.')

    # if value is successful, then it runs user_input through the pascal's triangle function
    list = Factorial(n)
    # print(Factorial.Aliminilab)
    #print(Factorial(5))

    # this is the input
    factorial = Factorial(n)
    print(factorial.output)
    print(factorial.work)


## make sure to change your input on lines 10 and 18 for the work() and fact()