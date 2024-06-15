n=input()
n=list(n)
for i in range(len(n)):
    n[i]=(eval(n[i])+5)%10
n.reverse()
for x in n:
    print(x,end='')
