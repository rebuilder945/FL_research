
def numbers(y):
    min=0;
    for x in y:
        if y.count(x)>min:
            min=y.count(x);
    return min;


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

