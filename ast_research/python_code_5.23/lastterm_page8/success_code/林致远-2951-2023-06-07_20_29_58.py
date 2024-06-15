def matrix(n=2): 
    s='* '*n
    for x in range(n):
      print(s.rstrip())

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

