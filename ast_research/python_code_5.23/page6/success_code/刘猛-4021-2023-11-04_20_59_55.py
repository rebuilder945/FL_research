stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
c = list(input())
d = ''
if int(c[0]) ==2:
    if int(c[-2]) ==0 and not int(c[-1]) ==0:
      for i in range(1,11):
        if i == int(c[-1]):
            d+=str(stu_list[i-1])
      e = eval(d)
      f = "".join(e)
      print(f)
    elif int(c[-2]) ==1:
      for i in range(1,11):
        if i == int(c[-1]):
            d+=str(stu_list[i+9])
      e = eval(d)
      f = "".join(e)
      print(f)
    elif int(c[-2]) ==2:
      d+=str(stu_list[19])
      e = eval(d)
      f = "".join(e)
      print(f)
    else:
       print("None")
else:
   print("None")
    


