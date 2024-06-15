# 读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。

lst = eval(input())
lst1 = []

def sushu(n):
    for i in range(2,n//2+1):
        if n %i == 0:
            return False
    return True

for n in lst:
    if sushu(n):
        lst1.append(n)

print(lst1)
