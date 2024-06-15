a=list[input()]
b=eval(input())
lst=a.split(",")
lst3=[]
for x in a:
    lst2 = [x,b.index(x)]
    lst3.append(lst2)
print(lst3)
    

