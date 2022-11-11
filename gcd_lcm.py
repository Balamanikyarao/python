from math import gcd
def gcd1(a,b):
    return gcd(a,b)
def lcm1(a,b):
    return a*b//gcd(a,b)
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
print("The gcd of two numbers is",gcd1(a,b))
print("The lcm of two numbers is",lcm1(a,b))
