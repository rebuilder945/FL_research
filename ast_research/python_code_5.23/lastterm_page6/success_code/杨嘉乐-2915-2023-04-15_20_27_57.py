x=eval(input())
open=0
for i in range(x+1):
    if i<=100:
        continue
    n=i
    l=[]
    while i!=0:
        l.append(i%10)
        i=i//10
    if l[0]**3+l[1]**3+l[2]**3==n:
        open=1
        print(i)
if open==0:
    print("none")
