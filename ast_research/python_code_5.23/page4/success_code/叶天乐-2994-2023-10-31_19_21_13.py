ls1 = list(input())
ls2 = []
for i in ls1:
    if i!=",":
        ls2.append(i)
n,m = eval(input())
ls3 = []
if n>len(ls2)-1 or n<-len(ls2):
    print("error")
else:
    ls3 = list(ls2[n])*m
    ls2+=ls3
    print(ls1)


