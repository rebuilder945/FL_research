def findigits(str):
      res,tmp="",""
      for x in str:
            if x>='0' and x<='9':
                  tmp+=x
            else:
                  tmp=""
            if len(tmp)>=len(res):
                  res=tmp
      return res

str=input()
print(findigits(str))
