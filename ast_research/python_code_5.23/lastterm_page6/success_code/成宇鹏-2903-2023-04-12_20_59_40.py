def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst = []
    c = 1
    for x in range(1,num+1):
        c = x*c
        b =1/c
        lst.append(b)  
        
    print("%.6f"%(1+sum(lst)))
main()


