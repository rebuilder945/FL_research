
input_list = eval(input())
ls=[]
i=len(input_list)
while i>=0:
    if list[i] not in ls:
        ls.append(list[i])
    i-=1 
ls.sort()   
print(ls)





