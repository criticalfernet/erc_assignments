def is_anagram(string1,string2):
    _list1 = list(string1.upper())
    _list1.sort()
    _list2 = list(string2.upper())
    _list2.sort()

    return _list1 == _list2

str1 = input("Enter the first string: ") 
str2 = input("Enter the second string: ") 

print(is_anagram(str1,str2))
