numend=input()
kon='m'
for i in range(len(numend)):
    a=int(numend[i])
    b=str((a+5)%10)
    kon+=b
end=kon[1:]

print(end[::-1])


