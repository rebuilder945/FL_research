#读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
lst = eval(input())
lst2 = []
for x in lst:
    for i in range(2,x-1):
        if x % i == 0:
            break
    else:
        lst2.append(x)
print(lst2)


