
#Method 1
def factorial(value):
    factvalue=1
    for i in list(range(1,value+1)):
        factvalue *=i
    print("Factorial of ",value, " is: ", factvalue)

a=int(input("Enter a Number: "))
factorial(a)

#Method 2

def factorialforloopwithreturn(value):
    factvalue=1
    for i in list(range(1,value+1)):
        factvalue *=i
    return factvalue

a=int(input("Enter a Number: "))
result=factorialforloopwithreturn(a)

print("Factorial of ",a, " is: ", result)

#Method 3

def factorialrecur(n):
    if(n<2):
        return 1
    else:
        return n* (factorialrecur(n-1))

a1=int(input("Enter a Number: "))
result1=factorialrecur(a1)
print("Factorial of ",a, " is: ", result1)
