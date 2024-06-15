import math
#由于拼写错误、对象被删除或重命名等原因导致无法导入
def godabach(m):
    if m <= 1:
        return False
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True

def huiwen_num(m):
    sm = str(m)
    sm1 = ""
    for y in sm:
        sm1 = y + sm1
    return sm1 == sm  # 直接返回判断结果

n = eval(input())
if math.floor(n) == n and n > 0:
    for m in range(n):
        if huiwen_num(m):
            if godabach(m):
                print(m, end=" ")
else:
    print("illegal input")