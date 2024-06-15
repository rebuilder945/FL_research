lst = input().split(' ')
stu = {}
stu["name"] = lst[0]
stu["english"] = lst[1]
stu["python"] = lst[2]
stu["math"] = lst[3]
sum = eval(lst[1])+eval(lst[2])+eval(lst[3])
avg = sum/len(stu)
stu["avg"] = avg
lst1 = list(map(int,lst[1:]))
lst1.sort()
print(lst[0],"%.2f %.2f %.2f"%(lst1[0],lst1[1],lst1[2]),avg)
