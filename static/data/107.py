num = input("请输入一个数字：")
num_list = [int(digit) for digit in num]

for i in range(len(num_list)):
    num_list[i] += 5
    num_list[i] = num_list[i] % 10
#问题出在尝试在整数上使用 len() 函数和对整数进行索引操作，
#这是因为 input() 函数返回的是字符串类型，而不是整数类型。

s = num_list[::-1]
print(s)