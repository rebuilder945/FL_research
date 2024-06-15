list1=eval(input())
list2=input().split(',')
n=int(list2[0])
m=int(list2[1])
if n>len(list1) or m>len(list1):
    print('error')
else:
    del list1[n:m]
    print(list1)
