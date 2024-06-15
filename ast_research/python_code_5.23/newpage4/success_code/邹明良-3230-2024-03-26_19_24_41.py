ls = list(eval(input()))
# print(ls)
# print(type(ls[0]))
ls.sort()
len=len(ls)
sum = 0
for i in range(len):
    a = int(ls.pop())
    sum += int(a*(10**(len-i-1)))
    # print(a,type(a),i,sum)
print(sum)


