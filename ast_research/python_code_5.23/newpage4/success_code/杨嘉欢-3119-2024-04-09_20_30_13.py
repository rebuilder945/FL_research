


input=eval(input())
print(input)
count=[]
for x in input:
    if x in count:
        continue
    else:
        count.append(x)
print(count)
