#要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。可以用sort排序来判断有没有重复的！
list1 = eval(input())        #切不可一边遍历列表，一边删除列表中的元素!!!我焯！注意输入东西时，如果要输入True就要大写T,因为python不认true，会说true is not defined
for x in list1:              #用copy函数就可以避免list的可变性造成的麻烦
    times=list1.count(x)
    if times > 1:
        list1.remove(x)
print(list1)  
