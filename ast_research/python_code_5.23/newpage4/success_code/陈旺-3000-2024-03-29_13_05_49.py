a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
c=sum(b)/len(b)
# if (int(c)-c)==0:
#     print(int(c))
# else:
print("%.2f"%(c))
