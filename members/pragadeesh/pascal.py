class pascalTriangle:  # Class is defined

    def __init__(self, num):  # Initialization procedure is defined; processes object num
        if num < 1 or num > 50:
            raise ValueError('Invalid Value')  # Uses selection to check for a valid value
        self._pascalList = []  # Program limits to 50 rows to avoid overflow on screen (frontend)
        matrix = [[0 for x in range(num)]
                  for y in range(num)]

        # Algorithm inspired by GeeksforGeeks
        # Matrix multiplication logic from Programiz

        for row in range(0, num):  # Iteration (for loop) runs through each index in the range and calculates the next row's values
            rowlist = []  # list for capturing each row is defined (list modified by algorithm)
            for column in range(0, row + 1):

                if column == 0 or column == row:  # Selection (if/else) is used to determine if the index is at the ends
                    matrix[row][column] = 1
                    print(matrix[row][column], end=" ")  # Printed when running tester code
                    rowlist.append(matrix[row][column])  # "rowlist" appends for column beginnings/ends

                else:
                    matrix[row][column] = (matrix[row - 1][column - 1] + matrix[row - 1][column])
                    print(matrix[row][column], end=" ")  # Printed when running tester code
                    rowlist.append(matrix[row][column])  # "rowlist" appends for middle columns
            print("\n", end="")
            self._pascalList.append(rowlist)  # Appends formatted data from "rowlist" into the list

    @property  # Property decorator
    def pascalList(self):  # Program's list is defined here for use in the backend
        return self._pascalList


# Driver Code
if __name__ == "__main__":
    while True:
        try:
            user_input = int(input('Please enter an integer value: '))  # Asks user for integer value
            # If user doesn't input an integer or inputs a number larger than 50, it will raise the ValueError
            if user_input > 50:
                raise ValueError
            break
        # ValueError sends an error message
        except ValueError:
            print('Invalid value or value too large. Please try again.')
    # If value is successful, then it runs user_input through the pascal's triangle function
    pascal = pascalTriangle(user_input)  # Call to the pascalTriangle procedure
    print(pascal.pascalList)  # Prints the final appended list "pascalList"
