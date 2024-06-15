names=list(map(str,input().split(',')))
scores=eval(input())
print([[names[i]]+[scores[i]] for i in range(len(names))])
