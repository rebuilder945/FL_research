def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=a
    n=0
    m=a
    if n<a:
        s+=m*10**n
        n+=1
        print(s)
main()

