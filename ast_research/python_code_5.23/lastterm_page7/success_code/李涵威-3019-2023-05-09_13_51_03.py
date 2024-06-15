name,*gradeList = input().split(" ")
gradeList = list(map(int,gradeList))
gradeList.sort(reverse=True)
gradeList.append(sum(gradeList)/len(gradeList))
gradeList.insert(0,name)
for x in gradeList:
    print(f"{x:.2f}" if isinstance(x,int) or isinstance(x,float) else x,end=" ")
