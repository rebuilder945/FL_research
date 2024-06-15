# #要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。可以用sort排序来判断有没有重复的！
# list1 = eval(input())        #切不可一边遍历列表，一边删除列表中的元素!!!我焯！注意输入东西时，如果要输入True就要大写T,因为python不认true，会说true is not defined
# list2 = list1.copy()
# for x in list2:              #用copy函数就可以避免list的可变性造成的麻烦。比如【1，2，3】，for i in list1,如果i=1之后把2去掉了，那么下一个i 就不会=2，而会=3了
#     times=list1.count(x)       #不能一边遍历一边删除
#     if times > 1:
#         list1.remove(x)
# print(list1)  

# 法二：
ls = eval(input())
ls2 = []
for i in range(len(ls)):
    if ls[i:].count(ls[i]) == 1 :
        ls2.append(ls[i])
print(ls2)
# 法三：
# ls = eval(input())
# ls2 = []
# for i in ls[::-1]:
#     if i not in ls2:
#         ls2.append(i)
# print(ls2.reverse())
