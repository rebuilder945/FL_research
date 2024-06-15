def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    total=0
    for i in range(a):
        total+=int(str(a)*(i+1))
    print(total)    

        

main()

