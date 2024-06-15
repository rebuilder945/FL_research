n=eval(input())
sum=0
string=str(n)
for i in range(len(string)):
    a=(int(string[i])+5)%10
    sum+=a*10**((len(string)-i-1))
final=0
if len(str(sum))==3:
    a=str(sum)[0]
    b=str(sum)[1]
    c=str(sum)[2]
    final=int(c+b+a)
elif len(str(sum))==4:
    a=str(sum)[0]
    b=str(sum)[1]
    c=str(sum)[2]
    d=str(sum)[3]
    final=int(d+c+b+a)
elif len(str(sum))>=5:
    a=str(sum)[0]
    b=str(sum)[1]
    c=str(sum)[-1]
    d=str(sum)[-2]
    e=str(sum)[2:-2]
    final=int(c+d+e+b+a)
elif len(str(sum))==1:
    final=sum
elif len(str(sum))==2:
    a=str(sum)[0]
    b=str(sum)[1]
    final=int(b+a)
print(final)
