mima=input()
xingji=0
special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
for i in mima:
    if "0"<=i<="9":
        xingji+=1
    if "a"<=i<="z":
        xingji+=1
    if "A"<=i<="Z":
        xingji+=1
    if len(mima)>7:
        xingji+=1
    if i in special_chars:
        xingji+=1

print(xingji)
  
