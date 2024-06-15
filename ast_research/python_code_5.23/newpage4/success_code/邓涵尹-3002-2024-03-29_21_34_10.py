#nums = eval(input())
#a = sum(nums)/nums
#print(a)

def ps(lst):
    total = sum(lst)
    average = total / len(lst)
    # 判断小数部分是否为 0
    if round(average, 2) % 1 == 0:
        return int(round(average, 0))
    else:
        return round(average, 2)

lst = eval(input())
print(ps(lst))
