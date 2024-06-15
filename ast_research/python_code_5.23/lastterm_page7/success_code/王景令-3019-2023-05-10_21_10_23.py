stu = {}
stu['name'],stu['english'],stu['python'],stu['math'] = input().split()
ls1 = []
ls1.append(eval(stu['english']))
ls1.append(eval(stu['python']))
ls1.append(eval(stu['math']))
stu['avg'] = sum(ls1) / len(ls1)
ls1.sort(reverse=True)
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(stu['name'],ls1[0],ls1[1],ls1[2],stu['avg']))
