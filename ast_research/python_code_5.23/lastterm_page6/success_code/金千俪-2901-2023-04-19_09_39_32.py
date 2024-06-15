a=input()
sum=0
lst=[]
while a!="#":
    sum=sum+int(a)
    lst.append(a)
    a=input()
print(len(lst),sum)
