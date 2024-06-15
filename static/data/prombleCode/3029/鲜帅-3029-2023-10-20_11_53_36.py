str1 = input()
name = [str(n) for n in str1.split(",")]
score = eval(input())
a = 0
b = len(name)
ls1 = []
while b > 0:
    ls2 = []
    ls2.append(name[a])
    ls2.append(score[a])
    ls1.append(ls2)
    a +=1
    b -=1
print(ls1)
