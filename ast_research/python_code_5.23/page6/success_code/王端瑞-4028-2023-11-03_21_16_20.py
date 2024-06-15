n = eval(input())

ls = []

if type(n)==int and n > 1:

    for i in range(n):

        k = 0

        for j in range(1,i+1):

            if i%j == 0:

                k+=1

        if k == 2:

            ls.append(i)

    for x in ls:

        if str(x) == str(x)[::-1]:

            print(x,end=" ")

else:

    print("illegal input")
