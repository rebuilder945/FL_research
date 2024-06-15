money=input().split(',')
card=eval(input())
cup=list(money)
water=()
tree=[]
for i in range(len(cup)):
    water=(cup[i],card[i])
    tree.append(list(water))
print(tree)
