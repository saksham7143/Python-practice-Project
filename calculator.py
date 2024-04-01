
###################################  CALCULATOR  ##########################################

def addition(num1,num2):
    sum = num1 + num2
    print("addition of ",num1,"and",num2,"is :- ",sum)
    
def subtract(num1, num2):
    sum = num1 - num2
    print("subtraction of ",num1,"and",num2,"is :- ",sum)

def multiple(num1, num2):
    sum = num1 * num2
    print("multiplaction of ",num1,"and",num2,"is :- ",sum)

def division(num1, num2):
    sum = num1 / num2
    print("division of ",num1,"and",num2,"is :- ",sum)


print("1.ADDITION")
print("2.SUBTRACTION.")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.EXIT")
n=0
while(n!=5):
    n=int(input("Enter You choice:"))
    if(n==1):
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        addition(a,b)
    if(n==2):
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        subtract(a,b)
    if(n==3):
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        multiple(a,b)
    if(n==4):
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        division(a,b)

