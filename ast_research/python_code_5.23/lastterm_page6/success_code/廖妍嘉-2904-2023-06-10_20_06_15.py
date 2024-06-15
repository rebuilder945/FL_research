def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    for i in range(1,a+1):
        b=[a]*i
        c=''.join(str(n) for n in b)
        d=int(c)
        ls.append(d)
    print(sum(ls))
main()

