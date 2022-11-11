class ShortInputException(Exception):
    def __init__(self,length):
        Exception(self)
        self.len=length
string=input("Enter The String")
length=len(string)
try:
    if length<3:
        raise ShortInputException(length)
except ShortInputException as s:
    print("The Length of String Is 3 Or Greater Than 3.\nBut Your Entered String Length Is",s.len)
else:
    print("No Exception")
    
