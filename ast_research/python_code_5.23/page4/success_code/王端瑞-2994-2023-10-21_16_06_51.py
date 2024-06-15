ls1 = input().split(",")

ls2 = []

ls3 = []

n,m = eval(input())

if n<len(ls1):

    for i in ls1:

        d = int(i)

        ls2.append(d)

    for a in ls2:

        if not a==ls2[n]:

            ls3.append(a)

        else:

            r = a

            ls3.append(a)

    for k in range(m):

        ls3.insert(len(ls3),r)

    print(ls3)

else:

    print('error')
