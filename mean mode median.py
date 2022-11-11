from statistics import mean,median,mode
l=[]
elesize=int(input("Enter the size of the list"))
print("Enter the list elements upto",elesize)
for i in range(elesize):
    ele=int(input())
    l.append(ele)
print("The list is",l)
print("The mean of given list is",mean(l))
print("The median of given list is",median(l))
print("The mode of given list is",mode(l))
