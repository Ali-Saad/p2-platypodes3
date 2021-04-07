# factors of a number in a class
class Factor:
    def __init__(self, num):
        if num < 0 or num > 1000000:
            raise ValueError("Value must be between 0 and 1 000 000")

        self._list = []

        #self.factor_number()
        factor = []
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
                factor.append(i)
        self._list.append(factor)


    @property
    def list(self):
        return self._list

if __name__ == "__main__":
    while True:
        try:
            # asks user for an integer value
            num = int(input('Enter a number to find its factors: '))
            # if user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
            if num > 1000000 or num < 0:
                raise ValueError
            break
        # ValueError sends an error message
        except ValueError:
            print('Invalid value or value too large. Value must be between 0 and 1 000 000. Please try again.')
    # if value is successful, then it runs user_input through the pascal's triangle function
    list = Factor(num)
    print(list.list)



