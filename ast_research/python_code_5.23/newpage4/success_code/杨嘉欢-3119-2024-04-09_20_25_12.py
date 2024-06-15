

input=input()
input=input[1:-1]
input=list(map(int and str,input.split(",")))
count=[]
for x in input:
    if x in count:
        continue
    else:
        count.append(x)
print(count)
