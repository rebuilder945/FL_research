lst=eval(input())
end=float(sum(lst)/len(lst))
flo=float(end-int(end))
if flo==0:
    print(int(end))
else:
    print('%2f'%(end))


