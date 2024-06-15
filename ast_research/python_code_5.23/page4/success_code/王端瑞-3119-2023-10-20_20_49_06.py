ls1 = eval(input())

ls2 = []

for i in ls1[-1::-1]:

    if i not in ls2:

        ls2.insert(0,i)
    
    else:

        continue

print(ls2)
