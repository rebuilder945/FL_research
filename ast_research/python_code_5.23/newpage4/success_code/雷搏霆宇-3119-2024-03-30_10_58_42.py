# a = list(eval(input()))
# # b = []
# for i in a:
#     t = a.count(i)
#     if t != 1:
#         a.remove(i)
# print(a)
a = list(eval(input()))
b = []
for i in a:
    b.append(i)
    for x in b:
        t = b.count(x)
        if t != 1:
            b.remove(x)
        
print(b)





