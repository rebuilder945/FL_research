#student  =  eval(input())
#print(student)
#print(student[1])
#print(type(student[1]))
#print(tuple(student[1].split('1')))
#info  =  (student[1])+(student[2])

#avg  =  sum(student[5])/len(student[5])

#print(info)
#print("%.2f"%avg)

#lst=list(input().split(','))
#bst=eval(input())
#cst=[[lst[i],bst[i]]for i in range(len(lst))]
#print(cst)
lst=eval(input())
bst=[]
def f(x):
    for i in range(2,x):
        if x%i==0:
            return False
            break
    return True
for x in lst:
    if f(x)==True:
        bst.append(x)
print(bst)


