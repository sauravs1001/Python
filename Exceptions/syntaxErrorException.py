try:
    dates = eval(input("Enter date : "))

except SyntaxError:
    print("Invalid date entered")

else:
    print("you entered :", dates)