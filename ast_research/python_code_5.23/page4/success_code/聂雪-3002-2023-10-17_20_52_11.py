ls=eval()
a=sum(ls)/len(ls)
if type(a)==int:
    print(a)
else:
    print('%.2f'%a)
