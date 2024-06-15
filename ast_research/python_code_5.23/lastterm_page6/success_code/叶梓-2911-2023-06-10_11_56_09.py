n = eval(input())
List1 = [int(x) for x in n]
for i in range(len(List1)):
    List1[i] = (List1[i] + 5) % 10    #除法运算：/---普通除法； //---整除； %---取余数
if len(List1) % 2 == 0:
    for y in range(int(len(List1) / 2)):
            temp = List1[y]           #temp是指？
            List1[y] = List1[-y-1]
            List1[-y-1] = temp
else:
    for z in range(int((len(List1) - 1) / 2)):
            temp = List1[z]
            List1[z] = List1[-z-1]
            List1[-z-1] = temp
List2 = [str(f) for f in List1]
num2 = str("".join(List2))          #？？？
print(num2)
