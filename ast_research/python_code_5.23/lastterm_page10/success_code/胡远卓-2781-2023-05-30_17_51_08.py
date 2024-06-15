def check(str):
      if len(str)!=18:
            return "Error"
      lst=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
      res=0
      for i in range(len(str)-1):
            res=(res+int(str[i])*lst[i])%11
      p=int(str[-1]) if str[-1]!='X' else 10
      if (12-res)%11==p:
            return "Correct"
      else:
            return "Wrong"

str=input()
print(check(str))
