def Anagram_Palindrome(s):
    count = [0 for i in range(0, 256)]
    odd = 0
    for i in s:
        count[ord(i)] += 1

    for i in range(0, 256):
        if count[i] & 1:
            odd += 1
    if odd > 1:
        print("String not anagram")
        return
    else:
        print("String anagram")
        return


s = input("Enter string ")
Anagram_Palindrome(s)
