M=eval(input())
Max=max(M)
Min=min(M)
Max1=M.count(Max)
Min1=M.count(Min)
if(Max==Min):
    print([])
else:
    for i in range(Max1):
        M.remove(Max)
    for i in range(Min1):
        M.remove(Min)
    print(M)  
