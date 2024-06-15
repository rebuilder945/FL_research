a=eval(input())
b,c=max(a),min(a)
if b in a:
    a.remove(b)
if c in a:
    a.remove(c)
print(a)
