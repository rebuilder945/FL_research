input_list=eval(input())
n=sum(input_list)/len(input_list)
if n - int(n) == 0:
    print(int(n))
else:
    print("{:.2f}".format(n))
