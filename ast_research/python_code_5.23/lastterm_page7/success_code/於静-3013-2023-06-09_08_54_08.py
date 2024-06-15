shuju=[]
while True:
    yuansu=input.split(' ')
    if yuansu !=["ok"]:
        shuju.append(yuansu)
    else:
        pass
        break
zidian=dict(shuju)
key=[]
value=[]
for i,j in zidian.items():
    key.append(i)
    value.append(int(j))
key.sort()
value.sort()
print(key)
print(value)
if "India" not in key:
    print("no")
else:
    pass
    print("yes")
sums=sum(value)
print(sums)


    
