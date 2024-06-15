def maxsum(mm):
    n=len(mm)/2
    fin=[]
    i=0
    if len(mm)>=2:
        a=random.sample(mm,2)
        fin.append(sum(a))
        mm.remove(a[1])
        mm.remove(a[0])
    else:
        return min(fin)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

