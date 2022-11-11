def length(str1):
    if str1=="":
        return 0
    else:
        return length(str[1:-1])
str1=input("Enter the  Data:")
print("The Length of the Data:",len(str1))
if str1==str1[::-1]:
    print("The Given Data:",str1, "is Palindrome")
else:
    print("The Given Data:",str1, "is not Palindrome")
          
