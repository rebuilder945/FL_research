lst=eval(input())
lstR=[]
for x in lst [::-1]:
    if x not in lstR:
        lstR.append(x)
print(lstR[::-1])

