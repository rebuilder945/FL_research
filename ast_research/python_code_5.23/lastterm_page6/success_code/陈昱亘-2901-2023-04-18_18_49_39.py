i=0
lst=[]
a=input()
while a!="#":
    lst.append(int(a))
    i+=1
    a=input()
print(int(i),int(sum(lst)))
