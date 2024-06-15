lst1=eval(input())
lst1.sort(reverse=True)
maxun=""
for i in range(len(lst1)):
    maxun=maxun+str(lst1[i])
maxun=eval(maxun)
    

print(maxun)
