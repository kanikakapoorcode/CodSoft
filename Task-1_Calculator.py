#Calculator 
print("------------------------CALCULATOR---------------------------")

print("\n")

print("Welcome to the Calculator,For Moving Further Click Enter: \n")

num1 = int(input("\nEnter the First Number: "))
num2 = int(input("Enter the Second Number: "))
print("\n-----------Now Choose the Operation from Below--------------")
print("Enter 1 for Addition\"+\" --->")
print("Enter 2 for Subtraction\"-\"--->")
print("Enter 3 for Multiplication\"*\"--->")
print("Enter 4 for Division\"/\"--->")
print("Enter 5 for Modulus\"%\"--->")
print("Enter 6 for Exponentiation\"**\"--->")
print("Enter 7 for Power\"^\"--->")
print("Enter 8 for Square root --->")
print("Enter 9 for Cube root --->")
print("Enter 10 for Factorial --->")


Choice = int(input("\n\nChoose the Operator You want to Perform- "))

if Choice == 1 :
    sum = 0
    sum = num1 + num2 
    print("\n****Addition of", num1 ,"and", num2 , "is" , sum)
elif Choice == 2 :
    sub = 0
    sub = num1 - num2
    print("\n****Subtraction of", num1 ,"and", num2 , "is", sub)
elif Choice == 3 :
    product = 1
    product = num1 * num2
    print("\n****Multiplication of", num1 ,"and", num2 , "is", product)
elif Choice == 4 :
    print("\n****Division of", num1 ,"from",num2,"is", num1/num2)
elif Choice == 5 :
    print("\n****The Modulus of", num1 ,"and",num2 ,"is",num1%num2)
elif Choice == 6 :
    print("\n****The Exponentiation of", num1 ,"and",num2 ,"is",num1**num2)
elif Choice == 7 :
    print("\n****The Power of", num1 ,"and",num2 ,"is",)

