def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a = int(input()) 
    a = str(a)
    lst = []
    lst.append(a)
    ax = []
    for i in range(1,int(a)+1):
        if len(lst[i-1]) <= i:
            b = lst[i-1] + a
        else:
            pass
        lst.append(b)
    result = ",".join(lst)
    for x in lst:
        x = int(x)
        ax.append(x)
    reason = sum(ax)
    print(reason)
main()

