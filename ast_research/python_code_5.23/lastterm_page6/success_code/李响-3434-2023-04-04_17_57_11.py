a = {'red','blue'}
b = {"red","yellow"}
c = {'yellow','red'}
m = input()
n = input()
if m and n in a and m != n :
    print("purple")
elif m and n in b and m != n:
    print("orange")
elif m and n in c and m != n:
    print("green")
else:
    print("error") 


