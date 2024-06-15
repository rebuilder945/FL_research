def matrix(n=2): 
        c=0
        d=0
        str=""
        while True:
            if c ==int(n):
                break
            else:
               str+="* "
               c+=1
        while True:
            if d ==int(n):
                 break
            else:
                print(str)
                d+=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

