n=eval(input())
n.sort(reverse=True)
num_str="".join(str(x) for x in n)
print(int(num_str))
