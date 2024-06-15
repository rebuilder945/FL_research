def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(n):
    s=0
    for i in range(1,n+1):
        b=str(n)*i
        s+=int(b)
    return(s)
main()

