def matrix(n=2): 
    if n==2:
        print("* *","\n","* *")
    else:
         for i in range(n):
              s += "* "
         for i in range(n):
             print(s,"\n")
             
        

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=int(number))  #有实参调用自定义函数

