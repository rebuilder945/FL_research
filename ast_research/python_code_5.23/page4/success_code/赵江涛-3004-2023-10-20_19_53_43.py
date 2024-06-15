ls = eval(input())
for i in range(len(ls)):
    for j in range(1,ls[i]):
       if ls[i]%j ==0:
        ls.pop(ls[i])
        print(ls)

