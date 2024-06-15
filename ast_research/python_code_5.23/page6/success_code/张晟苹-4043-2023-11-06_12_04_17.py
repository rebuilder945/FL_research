a=eval(input())
for i in a:
    for y in range(97,123):
        if chr(y) in i:
            print('%s,%d'%(chr(y),i.count(chr(y))))
        




