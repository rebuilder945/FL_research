a = eval(input())
lst = []
for i in a:
    for b in range(1,max(a)):
        if b != i:
            if i%b != 0:
                lst.append(i)
print(lst)

