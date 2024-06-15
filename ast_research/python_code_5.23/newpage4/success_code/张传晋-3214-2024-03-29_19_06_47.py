lst = eval(input())
num = lst.count(0)
for i  in range(num):
    lst.remove(0)
    lst.append(0)
print(lst)
