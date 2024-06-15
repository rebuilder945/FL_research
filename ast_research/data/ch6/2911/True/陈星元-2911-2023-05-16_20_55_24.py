num=input()
string=""
for x in num:
    y=str((int(x)+5)%10)
    string+=y
string1=string[::-1]
print(string1)


