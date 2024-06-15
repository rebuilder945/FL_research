def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    bb=len(tuple(a))
    ls1=[]
    ls2=[]
    while True:
        if 10**bb==1:
            break
        else:
            bb-=1
            ls1.append(bb)
        for x in ls1:
            s=a*10**x
            ls2.append(s)
    print(sum(ls2))
main()

