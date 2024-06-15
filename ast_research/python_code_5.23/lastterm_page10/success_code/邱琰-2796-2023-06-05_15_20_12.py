n=input()
for i in n:
    if i.isalpha():
        n=n.replace(i,' ')
ls=list(n.split(' '))
while 1:
    ls=ls.remove(' ')
ls2=[]
for i in ls:
    ls2.append(len(i))
for i in range(len(ls)-1,-1,-1):
    if ls2[i]>=max(ls2[0:i]):
        print(int(ls[i]))
