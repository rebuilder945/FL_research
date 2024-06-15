nums = eval(input())
zong = sum(nums)
end = zong/len(nums)
panduan = int(end)
if end%panduan == 0:
    print(panduan)
else:
    print("%.2f"%(end))
