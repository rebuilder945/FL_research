a=list(input().split(","))
b=input()
lst3=[]
for x in a:
    c=b[a.index(x)]
    lst2 = [1+x,c]
    lst3.append(lst2)
print(lst3)
    

