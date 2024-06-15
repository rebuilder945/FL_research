def remo(seq):
    uniqueele = []
    for ele in seq:
        if ele not in uniqueele:
            uniqueele.append(ele)
    return uniqueele

seq = eval(input())
s = remo(seq)
print(s)

