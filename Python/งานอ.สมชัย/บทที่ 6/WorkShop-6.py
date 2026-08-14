s = input("Enter username : ")
print()
if s.isalpha():
    print("Username is alphabetic")
    if s.lower() == "python":
        print("Username is 'python'")
    else :
        print("Username is not 'python'")
else :
    print("Username is not alphabetic")