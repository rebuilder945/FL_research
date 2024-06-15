names = input().split(",")
scores = input().split(",")
h = [ ]
for i in names:
    for x in scores:
        h.append(i+x)
print(h) 
    
