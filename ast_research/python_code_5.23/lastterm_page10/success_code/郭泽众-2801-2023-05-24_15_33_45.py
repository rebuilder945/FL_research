def isnum(x):
    if 48 <= ord(x) <= 57:
        return True

def islol(x):
    if ord('a') <= ord(x) <= ord('z'):
        return True

def iscal(x):
    if ord('A') <= ord(x) <= ord('Z'):
        return True

def isemo(x):
    caps = {'~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'}
    if x in caps:
        return True

a = 0
b = 0
c = 0
d = 0
e = 0
code = input()
for i in code:
    if isnum(i):
        a = 1
    if islol(i):
        b = 1
    if iscal(i):
        c = 1
    if isemo(i):
        d =1
if len(code) >= 8:
    e = 1
level = a + b + c + d + e
print(level)
