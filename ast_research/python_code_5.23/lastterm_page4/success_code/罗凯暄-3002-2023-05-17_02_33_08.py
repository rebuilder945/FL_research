ist = eval(input())
count = sum(ist)/len(ist)
if count % 1 == 0:
    print(int(count))
else:
    print("%.2f"% count)
