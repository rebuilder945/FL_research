lst=eval(input())
lst.sort()
num0=lst.count(0)
while 0 in lst:
    lst.remove(0)
for x in range(num0):
    lst.append(0)
print(lst)
