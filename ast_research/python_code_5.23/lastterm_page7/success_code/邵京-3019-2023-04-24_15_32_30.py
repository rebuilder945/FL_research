student=input().split()
gradelist=[]
for i in student:
    gradelist.append(i)
gradelistcopy=gradelist.copy()
del gradelistcopy[0]
gradelistcopy.sort()
for i in gradelistcopy:
    i=int(i)
    i='%.2f'%i
average=sum(gradelistcopy)/len(gradelistcopy)
print(gradelist[0],"".join(gradelistcopy),'%.2f'%average)



