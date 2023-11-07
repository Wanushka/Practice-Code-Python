#Question 04

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
def maximum(a,b,c):
    if(a>=b)and (a>=c):
        Largest = a
    elif (b>=a)and (b>=c):
        Largest = b
    else:
        Largest = c

    return Largest
print(maximum(a,b,c))


