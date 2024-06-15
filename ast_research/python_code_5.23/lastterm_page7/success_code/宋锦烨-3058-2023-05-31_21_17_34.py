dic={}
while True:
    a=input()
    if a =='q':
        break
    dic[a]=dic.get(a,0)+1
m = max(dic.values())
for x,y in dic.items():
    if y==m:
        print(x,y)
        break
