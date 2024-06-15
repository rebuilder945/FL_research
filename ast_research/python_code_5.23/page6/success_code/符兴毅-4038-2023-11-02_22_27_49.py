# 输入一行字符串，分别统计其中英文字母、空格、数字、和其他字符的个数
'''

思路：使用ord（）函数，利用ASCII判断字符类型

'''
a_list = input()
letter = []
space = []
nums = []
other = []
for i in range(len(a_list)):
    if ord(a_list[i]) in range(65,91) or ord(a_list[i]) in range(97,123):
        letter.append(a_list[i])
    elif a_list[i] == ' ':
        space.append(' ')
    elif ord(a_list[i]) in range(48,58):
        nums.append(a_list[i])
    else:
        other.append(a_list[i])

print('英文字母个数:%s'%len(letter))
print('空格个数:%s'%len(space))
print('数字个数:%s'%len(nums))
print('其他字符个数:%s'%len(other))




