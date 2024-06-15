lis = eval(input())
for i in lis.copy():
    if lis.count(i) > 1:
        lis.remove(i)
print(lis)
