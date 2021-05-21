# Defines header that will be printed in the beginning
def header():
    print("")
    print("-" * 35)
    print("Please Choose an Option to Continue")
    print("-" * 35)

# Defines a menu for users to pick from
def menu():
    print("Various Advanced Functions")
    print("1. Factors of a number")
    print("2. Sort a string of numbers")
    print("3. Factorial")
    print("4. Exit Calculator")

    # User input is taken here for menu select
    choice = input("Select an option: ")

    # Choices and paths based on user input
    if choice == "1":
        num = int(input("Enter a number to get its factors: " ))
        factor(num)
        header()
        menu()

        # Header and menu are called after the output of the algorithm to continue using the calculator

    if choice == "2":
        string = input("Enter a string (input numbers with commas in between with no spaces i.e. 5,4,3,2,1): ") # Input description
        sortedList = bubbleSort(string)

        print("\nOriginal List")
        print(sortedList.Original)

        print("\nSteps to sort the list:")
        print(sortedList.Iteration)

        print("\nSorted List")
        print(sortedList.Sorted)

        header()
        menu()

    if choice == "3":
        fact = 1
        n = int(input("Enter a number: "))
        for i in range(1 , n + 1):
            fact = fact * i
        print("The factorial of " + str(n) + " is: ",end="")
        print(fact)
        header()
        menu()

    if choice == "4":
        exit()


# Exit function
def exit():
    cont = input("Would you like to exit the calculator?\n(Y/N) ")
    if cont == "y":
        print("\nCome back soon!")
    else:
        header()
        menu()


# Factoring procedure and algorithm
def factor(x):
    print("The factors of", x ,"are...\n")
    for i in range(1, x + 1):
        # If there is no remainder, this is the result...
        if x % i == 0:
            print("A factor of the inputted number: " + str(i))
        # If there is a remainder, this is the result...
        if x % i != 0:
            print("Not a factor of the inputted number: " + str(i))

# Number sort procedure and algorithm in a class
class bubbleSort:
    def __init__(self, user_input):
        # Base python bubble sort algorithm taken from
        # https://www.geeksforgeeks.org/bubble-sort/

        self._Original = list(map(int, user_input.split(",")))
        self._Sorted = self._Original.copy()
        self._Iteration = []

        # Start of sort algorithm
        for i in range(len(self._Sorted) - 1, 0, -1):
            self._Iteration.append(self._Sorted.copy())
            for j in range(i):
                if self._Sorted[j] > self._Sorted[j + 1]:
                    temp = self._Sorted[j]
                    self._Sorted[j] = self._Sorted[j + 1]
                    self._Sorted[j + 1] = temp

    # The @property decorator is a pythonic way to use getters and setters in object-oriented programming
    @property
    def Sorted(self):
        return self._Sorted

    @property
    def Original(self):
        return self._Original

    @property
    def Iteration(self):
        return self._Iteration

if __name__ == "__main__":
    header()
    menu()