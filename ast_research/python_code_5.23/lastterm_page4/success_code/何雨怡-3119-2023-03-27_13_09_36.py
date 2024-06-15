lst=eval(input())
lst3=lst.reverse()
lstempty=[]
for i in lst3:
    if i not in lstempty:
        lstempty.append(i)
lstfinal=lstempty.reverse()
print(lstfinal)
