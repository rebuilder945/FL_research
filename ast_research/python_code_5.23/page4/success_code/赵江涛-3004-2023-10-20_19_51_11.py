ls = eval(input())
for i in range(len(ls)):
    for j in range(2,ls[i]):
       if ls[i-1]%j ==0:
        ls.pop(ls[i])
print(ls)

