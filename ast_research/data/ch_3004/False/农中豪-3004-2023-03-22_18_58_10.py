a=eval(input())
end=[]
for i in a:
    if i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break
            else:
                end.append(i)
print(end)
