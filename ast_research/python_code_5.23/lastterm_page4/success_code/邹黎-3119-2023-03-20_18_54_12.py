lst0=eval(input())
lstkong1=[]
lstkong2=[]
for i in  reversed(lst0):
    if i not in lstkong1 :
        lstkong1.append(i)
for i in reversed(lstkong1):
    if i not in lstkong2:
        lstkong2.append(i)
print(lstkong2)
