lst=eval(input())
lst.reverse()
lstempty=[]
for i in lst:
    if i not in lstempty:
        lstempty.append(i)
lstempty.reverse()
print(lstempty)
