ls1=list(input())
ls2=[]
ls3=[]
for i in ls1:
    if i=="X":
        ls2.append(10)
    else:
        ls2.append(int(i))
a="7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2"
a=a.split("－")
for i in a:
    ls3.append(int(i))
sum=0
if len(ls2)==18:
    for i in range(17):
        sum+=ls2[i]*ls3[i]
    sum=sum%11
    c=(12-sum)%11
    if c==ls2[17]:
        print("Correct")
    elif c!=ls2[17]:
        print("Wrong")
else:
    print("Error")

