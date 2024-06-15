def sushu(lst):
    final=[]
    
    for i in lst:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            final.append(i)
    return final
lst=eval(input())
result=sushu(lst)
print(result)
