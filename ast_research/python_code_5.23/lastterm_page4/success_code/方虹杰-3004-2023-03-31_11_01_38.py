def zhishu(num):
    if num in [0,1]:
        return False
    elif num in [2,3]:
        return True
    else:
        a=True
        for i in range(2,num):
            if num%i==0:
                a=False
                break
        return a
b=eval(input())
result=[x for x in b if zhishu(x)]
print(result)

