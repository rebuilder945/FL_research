up=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low=['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
shu=['0','1','2','3','4','5','6','7','8','9','0']
zhifu=['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '-', '/', ',', '.', '?', '<', '>', ';', ':', '[', ']', '{', '}', '|']
s=list(input())
xing=0
for i in s:
      if i in shu:  
        xing=xing+1
        break        
for i in s:
     if i in low:
        xing=xing+1
        break
for i in s:
     if i in up:
        xing=xing+1
        break
for i in s:
     if len(s)>=8:
        xing=xing+1
        break
for i in s:
     if i in zhifu:
        xing=xing+1
        break
print(xing)

