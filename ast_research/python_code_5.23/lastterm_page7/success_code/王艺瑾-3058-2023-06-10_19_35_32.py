x=[]
a=input()
while True:
    
    if a=="q":
        break
    else:
        x.append(a)
        a=input()
cishu=0
for i in x:
    if x.count(i)>cishu:
        cishu=x.count(i)
        zifu=i
print(zifu,cishu)

