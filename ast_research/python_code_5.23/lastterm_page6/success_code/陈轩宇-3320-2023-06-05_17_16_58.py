def main():
    chang = eval(input())
    kuan = eval(input())
    square(chang,kuan)
def square(chang,kuan):
    if chang == kuan:
        print("It's a square")
    elif chang != kuan:
        print("It's a rectangle")
    elif chang<0 or kuan<0:
        print("illegal data")
main()

