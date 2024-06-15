li1=list(eval(input()))
li2=eval(input())
n=int(li2[0])
m=int(li2[1])
if n>=len(li1) or n<-len(li1):
    print("error")
else:
    x=li1[n]
    for i in range(m):
        li1.append(x)
    print(li1)
