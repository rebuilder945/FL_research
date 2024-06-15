n=eval(input())
sum=0
ls1=[2,3]
ls2=[1,2]
if n<=2:
    for x in range(n):
        sum+=ls1[x]/ls2[x]
else:
    for x in range(n-2):
        i=ls1[x]+ls1[x+1]
        ls1.append(i)
        j=ls2[x]+ls2[x+1]
        ls2.append(j)
    for x in range(n):
        sum+=ls1[x]/ls2[x]
print("{:.4f}".format(sum))







