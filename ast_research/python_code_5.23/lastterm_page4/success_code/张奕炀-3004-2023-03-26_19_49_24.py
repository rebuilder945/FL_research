def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        return True
    else:
        return False

# def huiwenshu(n):
#     if str(n) == str(n)[::-1]:
#         return True
#     else:
#         return False

list1 = eval(input())
list2 = []
for i in range(len(list1)):
    if sushu(list1[i]):
        list2.append(list1[i])
print(list2)
