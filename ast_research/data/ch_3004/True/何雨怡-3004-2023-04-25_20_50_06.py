def sushu(lst):
    final=[]
    if 2 in lst:
        final.append(2)
    for i in lst:
        if i>2:
            for x in range(2,i):
                if i%x==0:
                    break
            else:
                final.append(i)
    return final
lst=eval(input())
result=sushu(lst)
print(result)
