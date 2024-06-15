from re import I


ls = eval(input())
ls2 = []
for i in range(len(ls)):
    for j in range(2,ls[i]):
        if ls[i]%j ==0:
            break
        else: ls2.append(ls[i])
        break 
            
print(ls2)

