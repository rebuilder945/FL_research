slist = input().split(' ')
stu={}
stu['name'] = slist[0]
stu['english'] = int(slist[1])
stu['python'] = int(slist[2])
stu['math'] = int(slist[3])
plist = [stu.get('english'), stu.get('python'), stu.get('math')]
stu['avg'] = sum(plist) / len(plist)
plist.sort()
plist.reverse()
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(stu.get('name'),plist[0],plist[1],plist[2],stu.get('avg')))
