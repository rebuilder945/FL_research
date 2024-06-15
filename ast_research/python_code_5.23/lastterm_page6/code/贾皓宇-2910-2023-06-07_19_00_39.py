
	# 定义一个空列表d
	d = []
	
	# 从文件中读取数据并将其存储到列表d中
	with open('cellpicture.txt') as f:
	    # 读取第一行数据，获取矩阵的行数m和列数n
	    m,n = map(int,f.readline().split())
	    # 读取剩余的行数据，将其转换为二维列表d
	    for x in range(m):
	        r = list(map(int, f.readline()[:n]))
	        d.append(r)
	
	# 定义一个函数，用于探索指定像素点的连通区域
	def explorePixel(d,m,n,i,j):
	        # 定义一个队列q，将起始像素点(i,j)加入队列中
	        q = [(i,j)]
	        # 当队列不为空时，循环执行以下操作
	        while q:
	            # 取出队列中的第一个像素点(x,y)
	            x,y = q.pop(0)
	            # 如果该像素点已经被标记为负数，则跳过
	            if d[x][y] < 0:
	                continue 
	            # 将该像素点标记为负数，表示已经被访问过
	            d[x][y] = 0-d[x][y]
	            # 将该像素点周围的未访问过的像素点加入队列中
	            if x>0 and d[x-1][y]>0:
	                q.append((x-1,y))
	            if x<(m-1) and d[x+1][y]>0:
	                q.append((x+1,y))
	            if y>0 and d[x][y-1]>0:
	                q.append((x,y-1))
	            if y<(n-1) and d[x][y+1]>0:
	                q.append((x,y+1))
	
	iCellCount = 0
	# 遍历整个矩阵，对于每个未访问过的像素点，执行explorePixel函数，统计连通区域的数量
	for i in range(m):
	    for j in range(n):
	        if d[i][j] <= 0:
	            continue
	        iCellCount += 1
	        explorePixel(d,m,n,i,j)
	        
	# 打印细胞个数
	if __name__=="__main__":
	    print(iCellCount)

