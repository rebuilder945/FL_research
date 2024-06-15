x=[]
while True:
    a=eval(input())
    if a!="q":
        break
    else:
        x.append(a)
cishu=0
for i in x:
    if x.count(i)>cishu:
        cishu=x.count(i)
        zifu=i
print(zifu,cishu)

