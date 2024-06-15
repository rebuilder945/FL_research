ls1 = eval(input())

sum = 0

for  i in ls1:

    sum = sum+i

ave = sum/len(ls1)

if ave%1==0:

    print(int(ave))

else:

    print('%.2f'%ave)
