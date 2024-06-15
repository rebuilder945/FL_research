'''
读入一个列表lst和正整数n和m，然后删除n~m之间的元素，
不包括m位置的元素，其中n小于或者等于m。如果输入的n和m不在列表lst的下标范围内，则输出"error"。
'''
a=list(eval(input()))
n,m=eval(input())
if m > len(a) or n <0:
   print(error)
else:
    for i in range(n,m):
        del a[n]
    print(a)
