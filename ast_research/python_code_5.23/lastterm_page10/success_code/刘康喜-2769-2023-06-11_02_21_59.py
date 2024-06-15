a=input()
print(a)
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d='abcdefghijklmnopqrstuvwxyz'
c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
e=d.upper()

for i in(a):



   if i in b and d.find(i)!=-1:
      f=b[26-d.find(i)-1]
   elif i in c and e.find(i)!=-1:
      f = c[26 - e.find(i)-1]
   else:
      f=i
   print(f,end='')


