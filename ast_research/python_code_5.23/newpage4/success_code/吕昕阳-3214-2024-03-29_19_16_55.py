lst=eval(input())
zero=lst.count(0)
while lst.count(0)>0:
    lst.remove(0)
zeros=[0]*zero
lst=lst+zeros
print(lst)
