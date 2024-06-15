lst0=eval(input())
lstkong1=[]
lstkong2=[]
for i in  reversed(lst0):
    if i not in lstkong1 :
        lstkong1.append(i)
lstkong1.reverse()
print(lstkong1)

