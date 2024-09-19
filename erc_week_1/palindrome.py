def check_palindrome(string):
    reversed = string[::-1]
    return reversed == string


str = input("Enter the string: ")
print(check_palindrome(str))
