lst=eval(input())
sushu=[]
for i in lst:
    for x in range(2,i):
        if i%x!=0:
            sushu.append(i)
print(sushu)
