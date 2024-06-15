def main():
    a=int(input())
    calculate_sum(a)
def calculate_sums():
    a = int(input()) 
    a = str(a)
    lst = []
    lst.append(a)
    ax = []
    if int(a) == 1:
        reason = 1
    else:
        for i in range(1,int(a)):
            if i < int(a):
                b = lst[i-1] + a
            else:
                pass
            lst.append(b)
        # result = ",".join(lst)
        for x in lst:
            x = int(x)
            ax.append(x)
        reason = sum(ax)
    print(reason)
main()

