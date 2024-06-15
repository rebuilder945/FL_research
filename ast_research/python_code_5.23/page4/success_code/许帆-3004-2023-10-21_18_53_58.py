a = eval(input())
lst = []
for i in a:
    for b in range(2,max(a)):
        if i%b == 0:
                break
        else:
            lst.append(i)
print(lst)

