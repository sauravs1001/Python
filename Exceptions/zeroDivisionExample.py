try:
    f = open("myfile", "w")
    # a = int(input("Enter a number"))
    # b = int(input("Enter another number"))

    a, b = [int(x) for x in input("Enter two numbers: ").split()]  # Written using list comprehension
    c = a/b
    f.write("writing %d into my file" %c)

except ZeroDivisionError:
    print("Division by zero not allowed, Enter some other number")

finally:
    f.close()
    print("file closed")