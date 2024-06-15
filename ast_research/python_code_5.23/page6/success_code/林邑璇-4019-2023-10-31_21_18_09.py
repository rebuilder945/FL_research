a=eval(input())
b=a
j=0
while b>=1:
        b=b//10
        j+=1
s=[]
for i in range(j):
        i=a%10
        d=(i+5)%10
        a=int((a-a%10)/10)
        s.append(d)
for i in s:
        print(i,end="")


