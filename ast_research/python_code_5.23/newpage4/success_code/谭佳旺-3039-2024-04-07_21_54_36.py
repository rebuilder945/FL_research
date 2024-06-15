lis1 =eval(input())
a =max(lis1)
b =min(lis1)
for i in lis1:
    if i == a or i == b:
        lis1.remove(i)
print(lis1)
