def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    for i in range(a):
        b=a*(a-i)*10**i
        ls.append(b)
    print(sum(ls))
main()

