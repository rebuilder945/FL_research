def decode(s):
    mapping = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba")
    return s.translate(mapping)

input_str = input()
decoded_str = decode(input_str)
print(f" {input_str}")
print(f" {decoded_str}")
