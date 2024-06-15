lst=eval(input())
lst0=[]
for x in lst:
    if x not in lst0:
        lst0.append(x)
geshu=len(lst)-len(lst0)
if 0 in lst0:
    lst0.remove(0)
    geshu+=1
k=0
while True:
    if k!=geshu:
        lst0.append(0)
        k+=1
    if k ==geshu:
        break
print(lst0)
