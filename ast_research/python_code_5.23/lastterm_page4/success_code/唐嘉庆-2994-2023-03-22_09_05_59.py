a=eval(input())
b,c=eval(input())
lst=list(a)
if b >len(lst):
    print('error')
else:
    e=lst[b-1]
    jack=[e]*c
    print(lst+jack)



