test=str(input())
for i in range(len(test)):
    a=test[i]
    if test.count(a)>1:
        print(a)
        break
