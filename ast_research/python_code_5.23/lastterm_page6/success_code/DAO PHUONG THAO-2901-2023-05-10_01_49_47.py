count=0
res=0
num_str=""
while True:
   num_str=input()
   if num_str=="#":
       break
   res+=eval(num_str)
   count+=1
print(count,res)
