from termcolor import colored

'''
Function to print statement using func3
'''
def func3():
# Print statement function
    print "Print statement function 3 - world"

class MyClass(object):
# MyClass with 3 variables
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
    # Printing the 3 variables in BLUE
        print "Variables in BLUE: " + colored(self.var1, 'blue') + ", " + colored(self.var2, 'blue') + ", " + colored(self.var3, 'blue')

    def not_hello(self):
    # Printing the 3 variables in GREEN
        print "Variables in GREEN: " + colored(self.var1, 'green') + ", " + colored(self.var2, 'green') + ", " + colored(self.var3, 'green')

class MyChildClass(MyClass):
# MyChildClass which override the 'hello' method and print a different statement and Print the 3 variables in RED
    def hello(self):
    # Printing the 3 variables in BLUE
        print "Variables in RED: " + colored(self.var1, 'red') + ", " + colored(self.var2, 'red') + ", " + colored(self.var3, 'red')

# Separation of executable code from importable code
if __name__ == "__main__":
    print "Main program - world"
