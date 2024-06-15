la=input().split()
stu={}
stu['name']=la[0]
stu['english']=la[1]
stu['python']=la[2]
stu['math']=la[3]
lst=list(stu.values())
# print(lst1)
lst.remove(la[0])
# print(lst)
for i in range(len(lst)):
    lst[i]=int(lst[i])
lst.sort(reverse=True)
print(la[0],end=' ')
for i in lst:
    print('%.2f'%(i),end=' ')
lst=list(map(int,lst))
print("%.2f"%((sum(lst))/(len(lst))))
