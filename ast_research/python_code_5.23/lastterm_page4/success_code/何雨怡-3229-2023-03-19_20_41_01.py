list=eval(input())
listsorted=sorted(list)
len=len(list)
mun=0
for i in range(len):
    mun=mun+listsorted[i]*10**(i)
print(mun)
