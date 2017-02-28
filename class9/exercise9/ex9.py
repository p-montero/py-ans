#!/usr/bin/env python
'''
Write a Python script in a different directory (not the one containing mytest).
a. Verify that you can import mytest and call the three functions func1(), func2(), and func3().
b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
'''

from mytest import *
from termcolor import colored

# Main verification function
def main():
    print "\n Invoking function defined by func1 | ",
    func1()
    print "\n Invoking function defined by func2 | ",
    func2()
    print "\n Invoking function defined by func3 | ",
    func3()
# Using MyClass
    print "\n Invoking class defined by MyClass | \n \t"
    my_example = MyClass('Derek', 'Jeter', '1972-10-29')
    my_example.hello()
    print "\t"
    my_example.not_hello()
    print "end of class 9"

if __name__ == "__main__":
    main()
