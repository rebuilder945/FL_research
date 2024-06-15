Bigalpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
littlealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a = input()
print(a)
a1=list(a)
b = []
for i in a1:
    if i in Bigalpha:
        t = Bigalpha.index(i)
        t = 26-t+1
        b.append(Bigalpha[t-2])
    elif i in littlealpha:
        t = littlealpha.index(i)
        t = 26-t+1
        b.append(littlealpha[t-2])
    else:
        b.append(i)
print("".join(b))
