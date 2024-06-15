n,m,l=eval(input())
b=0
result_list=[n]
if b<m :
      a=n+l
      b=b+1
      result_list.insert(0,b)
if b>=m :
      print(reversed(result_list))
       
