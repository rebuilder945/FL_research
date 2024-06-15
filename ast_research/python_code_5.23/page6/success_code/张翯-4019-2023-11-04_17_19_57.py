a=list(input())
b=[int(x) for x in a]
lst=[]
for i in b:
    i=(i+5)%10
    lst.append(i)
lst.reverse()
lst1=[str(z) for z in lst]
print("".join(lst1))



