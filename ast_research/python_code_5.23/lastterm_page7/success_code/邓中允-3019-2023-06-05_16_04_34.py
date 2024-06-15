s=list(input().split(" "))
stu={}
stu['name']=s[0]
stu['english']=s[1]
stu['python']=s[2]
stu['math']=s[2]
avg=(int(s[1])+int(s[2])+int(s[3]))/3
lst1=[]
lst1.append(stu['english'])
lst1.append(stu['python'])
lst1.append(stu['math'])
lst1.sort(reverse=True)
lst1.insert(-1,avg)
print("{}{:.2f}{:.2f}{:.2f}{:.2f}".format(stu['name'],lst1[0],lst1[1],lst1[2],lst1[3]))



