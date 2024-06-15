def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    b=0
    ls=[]
    for i in range(0,x):
        b=b+x*10**i
        ls.append(b)
    print(sum(ls))
main()

