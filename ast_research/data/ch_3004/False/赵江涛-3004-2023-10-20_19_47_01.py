ls = eval(input())
for i in range(len(ls)):
    for j in range(2,ls[i-1]):
       if ls[i-1]/j ==0:
        ls.remove(ls[i-1])
print(ls)

