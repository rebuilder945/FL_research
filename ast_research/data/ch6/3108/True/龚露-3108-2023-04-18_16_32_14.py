lst = eval(input())
e = ''.join(lst)
for i in range(97,123):
    if e.count(chr(i))>0:
        print(chr(i),e.count(chr(i)),sep=',')


