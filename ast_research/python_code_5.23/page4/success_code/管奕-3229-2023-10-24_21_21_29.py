a=eval(input())
list=a.sort(reverse=True)
for x in list:
    if list.count(x)==1:
        print(x)
else:
    print('False')

