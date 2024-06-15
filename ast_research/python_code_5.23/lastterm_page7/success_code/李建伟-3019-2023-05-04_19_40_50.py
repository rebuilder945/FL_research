lst = input().split()
lst1 = []
for i in lst[1::]:
    i = float(i)
    lst1.append(i)
lst1.sort(reverse=True)
dic = {}
dic['name'] = lst[0]
dic['english'] = float(lst[1])
dic['python'] = float(lst[2])
dic['math'] = float(lst[3])
dic['avg'] = (float(lst[1])+float(lst[2])+float(lst[3]))/3
print("%s %.2f %.2f %.2f %.2f"%(dic['name'],lst1[0],lst1[1],lst1[2],dic["avg"]))

