a = eval(input())
zero = a.count(0)
while a.count(0)>0:
    a.remove(0)
zeros = [0]*zero
a = a +zeros
print(a)
