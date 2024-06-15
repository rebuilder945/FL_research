def is_valid_input(n, m):    """
    检查输入是否合法
    """
    if not n.isdigit() or not m.isdigit():
        return False
    n = int(n)
    m = int(m)
    if n >= m or n < 0:
        return False
    return True


def get_numbers(n, m):
    """
    获取符合条件的三位数
    """
    res = []
    for i in range(n, m):
        for j in range(n, m):
            for k in range(n, m):
                if i != j and i != k and j != k:
                    temp = i * 100 + j * 10 + k
                    res.append(temp)
    return res


# 读取输入，调用函数，并输出结果
n, m = input().strip().split()
if not is_valid_input(n, m):
    print("illegal input")
else:
    numbers = get_numbers(int(n), int(m))
    if not numbers:
        print("illegal input")
    else:
        print(" ".join(map(str, numbers)))

