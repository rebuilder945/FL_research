ls1 = eval(input())
cnt = ls1.count(0)
for i in range(cnt):
    ls1.remove(0)
    ls1.append(0)
print(ls1)
