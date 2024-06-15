s1=input()
s2=input()
sums1=[]
sums2=[]
for i in s1:
    sums1.append(i)
for j in s2:
    sums2.append(j)
sums1.sort()
sums2.sort()
if sums1==sums2:
    print(True)
else:
    print(False)
