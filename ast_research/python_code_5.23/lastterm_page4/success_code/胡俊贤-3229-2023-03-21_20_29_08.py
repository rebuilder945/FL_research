ls=eval(input())
a=[]
for i in ls:
    if ls.count(i)==1:
        a.append(i)
if a==[]:
    print('False')
else:
    a.sort(reverse=False)
    print(",".join('%s' %i for i in a))


