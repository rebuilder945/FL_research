#读入一个正整数列表，每个正整数都只有一位。把这些列表里面的数字，按位数组织成一个最大的整数，每个数字占据一位，不能重复使用。然后输出这个数字。例如列表[1,2,3,4] 可以组成1234, 或者4321等多个整数。输出最大整数。
list1 = eval(input()) #正整数！所以不用讨论全是0的情况！
list1.sort(reverse = True)
s = 0
for i in range(len(list1)):
    s = s + int(list1[i]) * 10**(len(list1)-i-1)
print(s)
