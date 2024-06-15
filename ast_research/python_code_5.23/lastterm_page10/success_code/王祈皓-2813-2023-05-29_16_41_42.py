def remove_substring(string, substring):
    result = string.replace(substring, "")
    return result



string = input()
substring = input()
result = remove_substring(string, substring)
print(result)
