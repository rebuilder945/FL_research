s=input()
a=[]
if s=='':
      print("None")
else:
    for i in s:
        if s.count(i)==1:
              a.append(i)
    print(a[0])




'''

for i in s:
        if s.count(i)==1:
            print(1)
            break
else:
        print("None")
'''
