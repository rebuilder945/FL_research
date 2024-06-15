def remo(seq):
    uniqueele = []
    for ele in reversed(seq):
        if ele not in uniqueele:
            uniqueele.append(ele)
    return uniqueele

seq = eval(input())
s = remo(seq)
s = s[::-1]
print(s)
