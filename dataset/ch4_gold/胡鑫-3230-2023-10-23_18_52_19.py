list = eval(input())
list.sort()
position=0
output=0
for x in list:
    output=output+x*10**position
    position+=1
print(output)
