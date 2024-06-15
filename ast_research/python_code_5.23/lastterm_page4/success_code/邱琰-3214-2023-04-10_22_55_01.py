lst=eval(input())
num=lst.count(0)
while 0 in lst:
    lst.remove(0)
for i in range(num):
    lst.append(0)
print(lst)
