names=list(input().split(","))
scores = eval(input())

combinet = []

for i in range(0,len(names)):
    combinet.append([names[i],scores[i]])

print(combinet)
