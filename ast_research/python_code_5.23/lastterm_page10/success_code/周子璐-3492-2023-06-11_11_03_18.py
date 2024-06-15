test=str(input())
k=0
for i in range(len(test)):
    a=str(test[i])
    if test.count(a)==1:
        print(a)
        k=k+1
        break
if k==0:
    print('None')
