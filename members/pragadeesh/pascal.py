# pascal triangle algorithm within a class
class Pascal:
    # function defined for pascal's triangle with parameter 'n'. This is the class object
    def __init__(self):
        # the range has n + 1 instead of n because range function (1, n - 1) interval
        # therefore, 1 must be added for just n
        # ex: n = 5. The range goes from 1, 5 and produces 5 rows. Using only (1, n) would only give 4 rows
        for row in range(1, self + 1):
            self._row = row
            # variable for starting value. Changing this will make the same pattern but with different starting values
            start = 1
            # ex: if n = 5. There are 5 rows. This loop would go through i as 1, 2, 3, 4, and 5
            for i in range(1, row + 1):
                # first number in every line is 1 (start = 1)
                print(start, end=" ")
                start = int(start * (row - i) / i)
            print("")

    @property
    def get_row(self):
        return self._row


# lines 16-27 for checking valid integer values
while True:
    try:
        # asks user for an integer value
        user_input = int(input('Please enter an integer value: '))
        # if user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
        if user_input > 50:
            raise ValueError
        break
    # ValueError sends an error message
    except ValueError:
        print('Invalid value or value too large. Please try again.')
# if value is successful, then it runs user_input through the pascal's triangle function
Pascal.__init__(user_input)

'''pascal's triangle is used to find binomial coefficients.
For example, (x+1)^6 will have the coefficients of the 
pascal's triangle's 7th row'''