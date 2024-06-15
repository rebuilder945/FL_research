lst=eval(input())
num0=lst.count(0)
while 0 in range(num0):
    lst.append(0)
print(lst)
