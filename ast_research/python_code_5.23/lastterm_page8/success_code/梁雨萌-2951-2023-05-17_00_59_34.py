def matrix(n=2): 
        word="* *"
        n = int(n)
        if n == 1:
            print("*")
        elif n == 2:
            print(word)
            print(word)
        else:
            for x in range (0,n-2,1):
                word = word + " *"
            for x in range (n):
                print(word)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
            matrix(number)  #有实参调用自定义函数

