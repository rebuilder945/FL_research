dic = {}
LS = []
while True:
    a = input()
    if a != 'q':
        LS.append(a)
    else:
        break
ls=[]
for i in LS:
    dic[i]=LS.count(i)
print(max(dic,key=dic.get),max(dic.values()))



