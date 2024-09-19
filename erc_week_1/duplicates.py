
def find_duplicates(string):
    chars = list(string.lower())
    found = []
    duplicates=[]
    for char in chars:
        if (char in found):
            duplicates.append(char)
        else:
            found.append(char)
    return duplicates

str = input("Enter the string: ")
print(find_duplicates(str))
