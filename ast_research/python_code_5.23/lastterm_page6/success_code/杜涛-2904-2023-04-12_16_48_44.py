def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst=[]
    for i in range(a):
        b = str(a)*(i+1) 
        lst.append(int(b))
    print(sum(lst))
main()

