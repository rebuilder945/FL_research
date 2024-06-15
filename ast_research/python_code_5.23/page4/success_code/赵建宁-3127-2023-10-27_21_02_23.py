n = eval(input())
a = [n for n in range(1,n+1)]
for i in range(1):
    a.insert(len(a),a[0])
    a.remove(a[0])
input(a)
