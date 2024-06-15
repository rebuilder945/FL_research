def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    c=a
    s=a
    for x in range(a-1):
        b=c+a*10**(x+1)
        s=s+b
        c=b
    print(s)    
main()

