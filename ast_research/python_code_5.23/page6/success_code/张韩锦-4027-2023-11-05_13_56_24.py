n=input()
lst=[]
count=1
while n!="#":
    lst.append(int(n))
    n=input()
    if n =="#":
        break
    count+=1
print(count,sum(lst))

