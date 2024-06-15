n = input()
s = 0
for x in n:
    if ord(x) in range(48,58):
        s = s+1
        break
for x in n:
    if ord(x) in range(97,123):
        s = s+1
        break
for x in n:
    if ord(x) in range(65,91):
        s = s+1
        break
if len(n)>=8:
    s = s+1
la = ['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|',"\\"]
for x in n:
    if x in la:
        s = s+1
        break
print(s)


