ls1 = eval(input())

ls2 = []

for i in ls1:

    if i == 0:

        ls2.append(i)

    else:

        c = ls2.count(0)

        if c == 0:

            ls2.append(i)

        else:

            ls2.insert(-c,i)

print(ls2)
