s = input()
n = {}
for x in range(26):
    n[chr(ord('a')+x)]=chr(ord('a')+25-x)
    n[chr(ord('A')+x)]=chr(ord('A')+25-x)
print(s)
for x in s:
    if '0'<=x<='9':
        print(x,end='')
    elif 'A'<= x <='Z' or 'a'<= x <='z':
        print(n[x],end='')
    else:
        print(x,end='')
#4sdf&13TBD
