def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    i=0
    while i<a:
        s+=a*10**i
        i+=1
main()

