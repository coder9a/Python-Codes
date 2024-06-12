def Anagram(s1, s2):
    if sorted(s1) == sorted(s2):
         print('Strings are anagram')
    else:
        print('Strings are not anagram')

s1 = input("Enter first string ")
s2 = input("Enter second string ")
Anagram(s1, s2)