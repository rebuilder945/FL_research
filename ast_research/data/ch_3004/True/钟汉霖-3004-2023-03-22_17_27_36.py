a=eval(input())
n=[]
for t in range(len(a)):
    if a[t] in [2,3,5,7,11,13,17,19,23,29,31,37,367,389,599,643]:
        n.append(a[t])
print(n)
