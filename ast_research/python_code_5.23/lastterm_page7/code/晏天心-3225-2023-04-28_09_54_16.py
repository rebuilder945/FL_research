def work(a) :
def work(a) :
      dic = { 0:1 }
      b = 1
      i = 1
      while i != a+1:
             b *= i
             dic[ i ] = b
             i += 1
      return dic
	

a = int(input())
ans = work(a)
print(ans)

