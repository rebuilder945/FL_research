num=eval(input())
zero=num.count(0)
while num.count(0) > 0:
    num.remove(0)
zeros=[0]*zero
num=num+zeros
print(num)

