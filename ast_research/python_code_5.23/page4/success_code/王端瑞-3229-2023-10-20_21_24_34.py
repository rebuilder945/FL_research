ls1 = eval(input())

ls2 = []

for i in ls1:

    if ls1.count(i)>1:

        continue
    
    else:

        ls2.append(i)

if ls2==[]:

    print('False')

else:

    ls2.sort()

    for i in ls2:

        if i<max(ls2):

            print(int(i),end=',')

        else:

            print(int(i),end="")
