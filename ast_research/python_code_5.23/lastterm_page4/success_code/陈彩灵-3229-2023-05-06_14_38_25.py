ls = eval(input())
ls.sort()
x=[]

for i in ls :
    if ls.count(i)==1:
        x.append(i)
if x==[]:
    print(False)
else:
    x=str(x)
    x=','.join([j for j in x if j !=' 'and j !=',' and j !='[' and j !=']'])
    print(x)
