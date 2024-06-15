dic={}
while True:
    a=input()
    if a =='q':
        break
    dic[a]=dic.get(a,0)+1
m = max(d.values())
for x,y in d.items():
    if y==m:
        print(x,y)
        break
