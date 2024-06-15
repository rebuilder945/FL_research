from audioop import reverse


l = eval(input())
l.sort(reverse=True)
s = ""
for i in l:
    i = str(i)
    s += i 
print(int(s))



