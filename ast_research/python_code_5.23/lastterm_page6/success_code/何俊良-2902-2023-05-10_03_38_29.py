def get_sum(n):
    a, b = 2, 1
    sum_num = 0
    for i in range(n):
        sum_num += a / b
        a, b = a + b, a
    return sum_num
n = int(input().strip())
sum_num = get_sum(n)
print("{:.4f}".format(sum_num))

