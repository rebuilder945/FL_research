n=eval(input())
string=str(n)
sum=0
for i in range(len(string)):
    new=(int(string[i])+5)%10
    sum=new*10**(len(string)-i-1)
if len(string)==3:
    stringsum=str(sum)
    a=sum//100
    b=(sum-a*100)//10
    c=sum-a*100-b*10
    final=a+b*10+c*100
    print(final)
elif len(string)==4:
    stringsum=str(sum)
    final=int(stringsum[::-1])
    print(final)
elif len(string)>=5:
    stringsum=str(sum)
    a=stringsum[0]
    b=stringsum[1]
    c=stringsum[-1]
    d=stringsum[-2]
    e=stringsum[2:(len(string)-2)]
    final=int(c+d+e+b+a)
    print(final)

