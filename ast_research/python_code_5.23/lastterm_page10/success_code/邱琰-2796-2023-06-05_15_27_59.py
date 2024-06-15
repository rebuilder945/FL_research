n=input()
l=[x for x in n]
for i in l:
    if i.isalpha():
        i=' '
a=''.join(l)
ls=list(a.split(' '))
while 1:
    ls=ls.remove(' ')
ls2=[]
for i in ls:
    ls2.append(len(i))
for i in range(len(ls)-1,-1,-1):
    while ls2[i]>=max(ls2[0:i]):
        print(int(ls[i]))
        break
    else:
        print('No digit')
