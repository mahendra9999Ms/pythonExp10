try:
    num=int(input("Enter a number:"))
    result=10/num
    print("Result:",result)
except ValueError:
    print("Error:invalid input! please enter a valid number.")
except ZeroDivisionError:
    print("Error:Division by zero!")
