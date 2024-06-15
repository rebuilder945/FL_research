list=eval(input())
for n in list:
    if n >= 2:       
        for i in range(2, n):
            if n % i == 0:
                list.remove(n)
    else:
        continue
print(list)

