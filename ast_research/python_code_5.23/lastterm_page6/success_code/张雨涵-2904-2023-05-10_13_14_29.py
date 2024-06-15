def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        d = [i*a*10**(a-i) for i in range (a+1)]
        s = sum(d)
        print(s)  
main()

