def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        lst = []
        for i in range (1,a+1):
            b = int(str(a)*i)
            lst.append(b) 
        print(sum(lst))       
main()

