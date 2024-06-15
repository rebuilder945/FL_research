lis = eval(input())
lis1=lis.copy()
for i in lis1:
    if lis.count(i) > 1:
        lis.remove(i)
print(lis)
