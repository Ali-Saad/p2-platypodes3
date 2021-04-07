# pascal triangle algorithm within a class
from builtins import ValueError, range, print, int, property, input


class Pascal:
    # function defined for pascal's triangle with parameter 'n'. This is the class object

    def __init__(self, num):
        if num < 0 or num > 20:
            raise ValueError('Invalid Value')
        self._pascal = []

        # the range has n + 1 instead of n because range function (1, n - 1) interval
        # therefore, 1 must be added for just n
        # ex: n = 5. The range goes from 1, 5 and produces 5 rows. Using only (1, n) would only give 4 rows
        for row in range(1, num + 1):
            # variable for starting value. Changing this will make the same pattern but with different starting values
            start = 1
            row_l = []
            # ex: if n = 5. There are 5 rows. This loop would go through i as 1, 2, 3, 4, and 5
            for i in range(1, row + 1):
                # first number in every line is 1 (start = 1)
                print(start, end=" ")
                row_l.append(start)
                start = int(start * (row - i) / i)
            self._pascal.append(row_l)
            print("")

    @property
    def pascal(self):
        return self._pascal


# testing with user inputs
# lines 16-27 for checking valid integer values
if __name__ == "__main__":
    while True:
        try:
            # asks user for an integer value
            user_input = int(input('Please enter an integer value: '))
            # if user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
            if user_input > 20:
                raise ValueError
            break
        # ValueError sends an error message
        except ValueError:
            print('Invalid value or value too large. Please try again.')
    # if value is successful, then it runs user_input through the pascal's triangle function
    pascal = Pascal(user_input)
    print(pascal.pascal)

'''pascal's triangle is used to find binomial coefficients.
For example, (x+1)^6 will have the coefficients of the 
pascal's triangle's 7th row'''
