def work(a) :
   dict = {}
   for i in range(0,a+1):
        if i == 0:
            dict[i] = 1
        else:
            m = 1
            for n in range(1,i+1):
               m *= n
            dict[i] = m
        return dict
	

a = int(input())
ans = work(a)
print(ans)

