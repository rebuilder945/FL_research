stu={}
a=eval(input())
lst=list(a)
lst.sort(reverse=True)
lst[0]=round(lst[0])
lst[1]=round(lst[1])
lst[2]=round(lst[2])
stu["name"]="lst[0]"
stu["english"]="lst[1]"
stu["python"]="lst[2]"
e=round((lst[0]+lst[1]+lst[2])/3,2)
stu["avg"]="e"
print(''.join([str(value) for value in stu.values()]))

