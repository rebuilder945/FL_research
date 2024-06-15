def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    y=0
    j=a
    while a>1:
        x=j*a*10**y
        j-=1
        y+=1
    print(x)
main()

