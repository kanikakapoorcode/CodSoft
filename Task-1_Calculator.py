#Calculator 
def CalculatePower(N,X):#user defined function for calculating Power
  P=1
  for i in range(1, X+1):
    P=P*N
  return P
print("*************************************************************")  
print("\n------------------------CALCULATOR---------------------------")
print("\n*************************************************************")

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
    print("\n****Addition of", num1 ,"and", num2 , "is--->" , sum)
elif Choice == 2 :
    sub = 0
    sub = num1 - num2
    print("\n****Subtraction of", num1 ,"and", num2 , "is--->", sub)
elif Choice == 3 :
    product = 1
    product = num1 * num2
    print("\n****Multiplication of", num1 ,"and", num2 , "is--->", product)
elif Choice == 4 :
    print("\n****Division of", num1 ,"from",num2,"is--->", num1/num2)
elif Choice == 5 :
    print("\n****The Modulus of", num1 ,"and",num2 ,"is--->",num1%num2)
elif Choice == 6 :
    print("\n****The Exponentiation of", num1 ,"and",num2 ,"is--->",num1**num2)
elif Choice == 7 :
    print("\n****The Power of", num1 ,"and",num2 ,"is--->",CalculatePower(num1,num2))
elif Choice == 8 :
    print("\n****The Square root of", num1 ,"is--->",num1**(1/2))
    print("\n****The Square root of", num2 , "is--->" ,num2**(1/2))
elif Choice == 9 :
    print("\n****The Cube root of", num1 ,"is--->",num1**(1/3))
    print("\n****The Cube root of", num2 ,"is--->",num2**(1/3))
elif Choice == 10 :
    fact1 = 1
    if num1 < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num1== 0:
       print("The factorial of 0 is 1")
    else:
      for i in range(1, num1+1):
       fact1 = fact1 * i
    print("\n****The Factorial of", num1 ,"is--->",fact1)
    fact2 = 1
    if num2 < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num2 == 0:
       print("The factorial of 0 is 1")
    else:
      for i in range(1, num2+1):
       fact2 = fact2 * i
    print("\n****The Factorial of", num2 ,"is--->",fact2)
    
else :
    print("\n****Invalid Choice, Please Try Again!!")
    
print("\n\n-----------------------------------------------")
print("\n****Thus the required answer is Calculated.****")
print("\n\n-----------------------------------------------")

