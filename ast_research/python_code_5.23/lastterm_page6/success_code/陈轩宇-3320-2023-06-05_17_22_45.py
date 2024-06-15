def main():
    chang = eval(input())
    kuan = eval(input())
    square(chang,kuan)
def square(chang,kuan):
    if chang>0 and kuan>0:
        if chang == kuan:
            print("It's a square")
        elif chang != kuan:
            print("It's a rectangle")
    else:
        print("illegal data")
main()

