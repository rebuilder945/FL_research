def main():
    a=int(input())
    calculate_sum(a)
        print(calculate_sum(a))
def calculate_sum(a):
    ls=[]
    for i in range(a):
        a=a*(10**i)
        ls.append(a)
    s=sum(ls)
    return s
main()

