def sumlist(lst1,x):
    jishu=0
    for i in lst1:
        if type(i)==int:
            jishu+=i*x
        elif type(i)==list:
            jishu+=sumlist(i,x+1)
    return jishu
    






nums = eval(input())
addv = sumlist(nums, 1)
print(addv)



