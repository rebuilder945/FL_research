a = input()
b = 0
c = [[0,1],[1,0],[2,"X"],[3,9],[4,8],[5,7],[6,6],[7,5],[8,4],[9,3],[10,2]]
e = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(a)!=18:
    print("Error")
else:
    for i in range(17):
        b = int(a[i])*e[i]+b
    d = b%11
    for j in c:
        if j[0]==d:
            if a[17]==str(j[1]):
                print("Correct")
            else:
                print("Wrong")
