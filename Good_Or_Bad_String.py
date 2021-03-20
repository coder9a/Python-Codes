def Good_Bad(str):
    v = c = 0
    lst = ['a','e','i','o','u']
    for i in str:
        if i in lst:
            v+=1
            c=0
        else:
            c+=1
            v=0
        if i=='?':
            c+=1
            v+=1

    if c>3 or v>5:
        print("BAD String")
        return
    else:
        print('GOOD String')
        return

s = input("Enter string ")
Good_Bad(s)






str = input("Enter String ")
Good_Bad(str)