ls1=list(input())
ls2=list(input())
if len(ls1)==len(ls2):
    for i in ls1:
        if i in ls2:
            ls1.count(i)==ls2.count(i)
    print('True')
else:
    print('False')





