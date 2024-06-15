ls=[x for x in range(1,eval(input())+1)]
ls1=[]
for i in range(1,len(ls)+1):
    ls1.append(ls[-i])
print(ls1)
