n=eval(input())
stringn=str(n)
newnum=0
for i in range(len(stringn)):
    cut=stringn[i]
    new=(int(cut)+5)%10
    newnum=newnum+new*10**(len(stringn)-i-1)
stringnew=str(newnum)
a=stringnew[0]
b=stringnew[1]
c=stringnew[-1]
d=stringnew[-2]
e=stringnew[2:(len(stringnew)-1)]
final=c+d+e+b+a
print(int(final))

