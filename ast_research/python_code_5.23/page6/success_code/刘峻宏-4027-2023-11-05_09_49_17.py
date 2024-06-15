a=[]
while True:
    b=input()
    if b =="#":
        break
    
    a.append(eval(b))
print(len(a), sum(a))
