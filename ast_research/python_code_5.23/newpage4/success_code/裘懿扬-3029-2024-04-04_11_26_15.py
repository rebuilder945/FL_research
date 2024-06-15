a=input()
b=list(eval(input()))
c=a.split(",")
j=[]
for x in range(0,len(c)):
    j.append([c[x],b[x]])
print(j)
