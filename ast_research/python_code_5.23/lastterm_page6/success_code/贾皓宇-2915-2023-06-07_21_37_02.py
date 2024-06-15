def search(x):
    a=list(str(x))
    for d in range(len(a)):
        a[d]=int(a[d])
    if a[0]**3+a[1]**3+a[2]**3==x:
        return x
t=eval(input())
s=[]
for y in range(100,t+1):
    if search(y)!=None:
        print(search(y))
        s.append(search(y))
if s==[]:
    print('none')
