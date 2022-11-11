#display the grade of the student based on average
sub1=int(input("Enter the sub1 marks"))
sub2=int(input("Enter the sub2 marks"))
sub3=int(input("Enter the sub3 marks"))
sub4=int(input("Enter the sub4 marks"))
sub5=int(input("Enter the sub5 marks"))
sum1=sub1+sub2+sub3+sub4+sub5;
avg=float(sum1/5)
print("The total marks obtained by the student is",sum1)
print("The avg marks obtained by student is",avg)
if avg>=90:
    print("Congratulations O grade")
elif avg>=80 and avg<90:
    print("Congratulations A+ Grade")
elif avg>=70 and avg<80:
    print("Congratulations A Grade")
elif avg>=60 and avg<70:
    print("Congratulations B+ Grade")
elif avg>=50 and avg<60:
    print("Congratulations B Grade")
elif avg>=40 and avg<50:
    print("Congratulations C Grade")
elif avg<40:
    print("Sorry Fail")
