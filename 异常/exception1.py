try:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    print x / y
except ZeroDivisionError:
    print "The second number can't be zero!"

except TypeError:
    print  "The second number is not a number, was it?"