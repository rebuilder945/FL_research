# a=input()
# a=a.strip("[")
# a=a.rstrip("]")
# b=[int(i) for i in a.split(",")]
# c=[]
# for i in b:
#     if i<2:
#        c.append(i)
#     elif i==2:
#        None
#     else:
#        for x in range(2,i):
#           if i%x==0:
#              c.append(i)
# for i in b:
#    if i in c:
#       b.remove(i)
# print(b)
a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
c=[]
yes=1
for i in b:
      if i<2:
         yes==0
      elif i==2:
         c.append(i)
      else:
         for x in range(2,i):
            if i%x==0:
               yes=0
               break
         if yes==1:
            c.append()
print(c)
        
           


