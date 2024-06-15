test=str(input())
for i in range(len(test)):
    a=str(test[i])
    if test.count(a)==1:
        print(a)
        break
    else:
        print('None')
