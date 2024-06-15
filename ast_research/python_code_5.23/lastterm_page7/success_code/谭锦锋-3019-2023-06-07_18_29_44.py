stu = {}
a,b,c,d = map(str,input().split(' '))
stu['name'] = a
stu['english'] = float(b)
stu['python'] = float(c)
stu['math'] = float(d)
avg = (float(b)+float(c)+float(d))/3
lst = []
lst.append(stu['english'])
lst.append(stu['python'])
lst.append(stu['math'])
lst.sort()
lst.reverse()
lst.insert(0,stu['name'])
lst.insert(4,avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(lst[0],lst[1],lst[2],lst[3],lst[4]))
