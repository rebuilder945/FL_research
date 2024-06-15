a=eval(input())
b=a.copy()
c=max(a)
d=min(a)
# print(d,c)
for i in b:
#      if c !=d:
#           if   c in a:
#                a.remove(c)
#           elif d in a:
#                a. remove(d)
#      elif c == d:
#           a.clear()
# print(a)
     if i == c or i == d:
          a.remove(i)
print(a)


