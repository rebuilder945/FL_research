aug=eval(input())
for x in aug:
    if x==0:
        aug.remove(x)
        aug.append(x)
print(aug)

            
