def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=str(a)
    n=[]
    for i in range(a):
        b=s*(i+1)
        n.append(int(b))
    print(sum(n))
main()

