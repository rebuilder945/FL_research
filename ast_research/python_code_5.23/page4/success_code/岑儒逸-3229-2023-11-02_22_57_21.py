ls=eval(input())
final=[]
for i in ls:
    if ls.count(i)==1:
        final.append(i)
if len(final)==0:
    print('False')
else:
    final.sort()
    for i in final[:-1]:
        print(i,end=",")
    print(final[-1])
