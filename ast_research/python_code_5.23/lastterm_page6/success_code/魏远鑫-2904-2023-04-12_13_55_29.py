def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    b=0
    ls=[]
    if x==10:
        for i in range(0,x):
            b=b+x*100**i
            ls.append(b) 
        print(sum(ls))
    else:
        for i in range(0,x):
            b=b+x*10**i
            ls.append(b)
        print(sum(ls))
main()

