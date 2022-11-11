def cummulative_product(n):
    l=[]
    product=1
    print("Read The List Of Elements Upto:",n)
    for i in range(n):
        ele=int(input())
        l.append(ele)
    for i in l:
        product=product*i
    return product
n=int(input("Enter Size Of List:"))
print("The Cummulative Product Of The List is:",cummulative_product(n))
              
