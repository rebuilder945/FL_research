def gaoji(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
list1=eval(input())
list2=[num for num in list1 if gaoji(num)]
print(list2)    


