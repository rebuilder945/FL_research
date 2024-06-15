def maxsum(nums):
    letter = nums
    n = 2
    fuck = [letter[i:i+n] for i in range(0,len(letter),n)]
    for x in fuck:
        b = min(x)
        shit = []
        shit.append(b)
    return(sum(shit))





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

