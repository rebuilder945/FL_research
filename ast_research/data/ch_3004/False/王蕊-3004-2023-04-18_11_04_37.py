lst=eval(input())
lst2=[]
for x in lst:
    if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
        lst2.append(x)
        print(lst2)
        

