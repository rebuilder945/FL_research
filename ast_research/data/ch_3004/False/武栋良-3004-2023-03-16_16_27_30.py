ls1 = eval(input('请输入列表：'))
ls2 = []
for x in ls1:
    for i in range(2,x):
        if x%i ==0:
            break
        else:
            ls2.append(x)
            break
print(ls2) 
