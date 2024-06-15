dic={}
while True:
    a=input()
    if a=="q":
        break
    else:
        dic[a]=dic.get(a,0)+1
max=0
for i in dic.items():
    if i >=max:
        i=max
for x in dic.keys():
    if dic[x]==max:
        print(x,max)
