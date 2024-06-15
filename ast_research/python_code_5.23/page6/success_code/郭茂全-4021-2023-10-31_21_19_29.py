a=eval(input())
list=[eval(input())]
r=list[0][0]
l=list[-1][0]
while (r<=l):
    m=(r+l)//2
    if (list[m][0]>a):
        r=m-1
    elif (list[m][0]<a):
        l=m+1
    elif (list[m][0]==a):
        print(m)
        break
else:
    print(None)
