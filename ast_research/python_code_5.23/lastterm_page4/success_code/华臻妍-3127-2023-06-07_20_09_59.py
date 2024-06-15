n = eval(input())
lst = [x for x in range(1,n+1)]#快速生成一个列表
lst1=[]
for i in range(n):
    m=(i+1)%n#第一次循环rangen（n）的i是0 i+1就是1  1/5余1所以m就是1 就把lst中下标为1的元素添入lst1,因为i+1肯定小于等于n,最后的i是n-1 i+1就是n 所以余数是0 就把原列表的第一位添到了最后
    lst1.append(lst[m])#lst用【】
print(lst1)

