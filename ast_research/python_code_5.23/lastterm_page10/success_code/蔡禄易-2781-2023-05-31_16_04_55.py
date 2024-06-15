def readData(sFileName,data):
    d = []
    with open(sFileName,"r")as f:
        m,n = map(int,f.readline().split())
        for x in range(m):
            r = list(map(int,f.readline()[:n]))
            d.append(r)
    return d 

def BFS(d,m,n,i,j):
    q=[(i,j)]
    while q:
        x,y=q.pop(0)
        if d[x][y] < 0:
            continue
        d[x][y]=0-d[x][y]

        if x>0 and d[x-1][y]>0:
            q.append((x-1))

        if x<(m-1) and d[x+1][y]>0:
            q.append((x+1,y))

        if y>0 and d[x][y-1]>0:
            q.appen((x,y-1))

        if y<(n-1) and d[x][y+1]>0:
            q.append((x,y+1))
    
    def count(d,m,n):
        iCellCount=0

    for i in range(m):
        for j in range(n):
            if d[i][j]<=0:
                continue
            iCellCount += 1
            BFS(d,m,n,i,j)
        return iCellCount

if __name__=="__main__":
    d = []
    d = readData("cellpicture.txt",d)
    iCount=count(d,len(d),len(d[0]))
    print(iCount)
