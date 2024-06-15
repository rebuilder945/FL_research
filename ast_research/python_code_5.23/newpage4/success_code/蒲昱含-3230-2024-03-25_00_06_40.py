list=[]
a=input()
list(eval(a))
list.sort
b=0
for i in range(len(list)):
    c=list[i]
    b+=c*(10**i)
print(b)
