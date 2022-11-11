a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))
list1=[1,2,3,4,5]
try:
    c=a/b
    print("The Division Result is",c)
    print(list1[10])
except (ZeroDivisionError,IndexError):
    print("Please see the try block their is exception\nIt may be Zero Division or Invalid Index")
else:
    print("No Exception")
finally:
    print("GoodBye!")
