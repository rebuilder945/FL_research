lines=[]
while True:
    line=(input())
    if line=="#":
        break
    lines.append(eval(line))
print(len(lines),sum(lines))

