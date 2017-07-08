while True:
    try:
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        print x / y

    except Exception, e:
        print "Invalid input: ,", e
        print "please try again!"

    else:
        break
