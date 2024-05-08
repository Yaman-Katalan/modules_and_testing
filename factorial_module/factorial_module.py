# factorial_iterative     >>> using loop
# factorial_recursion     >>> using recursion
# clumsy * /(floor) + -   >>> using either loop or recursion 

import math

def factorial_recursion(n):
    "This function calculates the factorial using recursion for any positive number."
    if n<1:
        return "Please enter a positive number!"
    if n==1:
        return n
    else:
        return n * factorial_recursion(n-1)

print("factorial_recursion") 
print(factorial_recursion(8))
print(factorial_recursion(7))
print(factorial_recursion(9))

def factorial_iterative(n):
    "This function calculates the factorial using while_loop for any positive number."
    if n<1:
        return "Please enter a positive number!"
    c=0
    result=1
    while n>c:
        c+=1
        result*=c
    return result


 


def clumsy(n):
    "This function calculates clumsy factorial for any positive number"
    if n<1:
        return "Please enter a positive number!"
    elif n==3:
        return 6
    elif n==2:
        return 2
    elif n==1:
        return 1
    
    i=n
    result=1

    a=i
    i-=1
    b=i
    i-=1
    c=i
    i-=1
    d=i
    i-=1

    result*= math.floor(a*b/c)+d
    # print(result)
    # print(f"i:{i}")

    while i>0:
        if i>=4:
            a=i
            i-=1
            b=i
            i-=1
            c=i
            i-=1
            d=i
            i-=1
            result-= math.floor(a*b/c)-d
            # print(result)
        
        elif i==3:
            a=i
            i-=1
            b=i
            i-=1
            c=i
            i-=1
            result-= math.floor(a*b/c)
            # print(result)
        
        elif i==2:
            a=i
            i-=1
            b=i
            i-=1
            result-=a*b
            # print(result)
        
        elif i==1:
            a=i
            i-=1
            result-=a
            # print(result)
        
        elif i==0:
            break
    return result





