list_1=eval(input())
a=max(list_1)
min=min(list_1)
for i in range(len(list_1)+1):
   if list_1[i]==a:
      list_1.remove(list_1[i])
   elif list_1[i]==min:
      list_1.remove(list_1[i])
      print(list_1)

