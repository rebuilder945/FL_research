# from tokenize import Number


# nums=input()
# NumList=[int(x) for x in nums.split(',')]
# def CountNum(num:NumList[NumList]):
#     n=NumList.count(num)
#     if n=1:
#     return i

# a=CountNum(num:NumList[NumList])
# print(a)
lists1=eval(input())
lists2=[]
def countnums(lists1):
    for i in lists1:
        n=lists1.count(i)
        if n==1:
            lists2.append(i)
    return lists2
lists2=countnums(lists1)
if len(lists2)==0:
    lists2.sort()
    print(lists2)

