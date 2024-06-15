lst1=eval(input())
lst1.sort()
maxun=0
for i in range(len(lst1)):
    maxun=maxun+lst1[i]*10**(i+1)
b=lst1.count(0)
maxun=maxun*10**b
print(maxun)
