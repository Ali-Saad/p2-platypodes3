class pascalTriangle:

    def __init__(self, num):
        if num < 0 or num > 100:
            raise ValueError('Invalid Value')
        self._pascalList = []
        # 2D array to store the values
        matrix = [[0 for x in range(num)]
                  for y in range(num)]

        # iterating through the rows
        for row in range(0, num):
            rowlist = []
            # iterating through each value of the row
            for column in range(0, row + 1):

                # first and last column are 0
                if column == 0 or column == row:
                    matrix[row][column] = 1
                    print(matrix[row][column], end=" ")
                    rowlist.append(matrix[row][column])

                # calculating the sum of the above two values
                else:
                    matrix[row][column] = (matrix[row - 1][column - 1] + matrix[row - 1][column])
                    print(matrix[row][column], end=" ")
                    rowlist.append(matrix[row][column])
            print("\n", end="")
            self._pascalList.append(rowlist)

    @property
    def pascalList(self):
        return self._pascalList


# Driver Code
if __name__ == "__main__":
    while True:
        try:
            # asks user for an integer value
            user_input = int(input('Please enter an integer value: '))
            # if user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
            if user_input > 100:
                raise ValueError
            break
        # ValueError sends an error message
        except ValueError:
            print('Invalid value or value too large. Please try again.')
    # if value is successful, then it runs user_input through the pascal's triangle function
    pascal = pascalTriangle(user_input)     # Pascal = class
    print(pascal.pascalList)


    '''num = int(input("Enter the number of rows: "))
    pascal = pascalTriangle(num)
    print(pascal.pascalList)'''