ls1 = eval(input())

ls2 = []

for i in ls1:

    k = 0

    for j in range(1,i+1):

        if i%j==0:

            k+=1

    if k == 2:

        ls2.append(i)

print(ls2)
