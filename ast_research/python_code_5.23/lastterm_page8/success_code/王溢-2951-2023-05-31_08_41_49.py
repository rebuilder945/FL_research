def matrix(n=2): 
    i=1
    j=1
    while i<=n:
      while j<n:
        print("*",end=" ")
        j+=1
      print("*")
      i+=1
      j=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

