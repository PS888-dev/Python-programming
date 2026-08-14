s = input("Enter string : ")
print()
if (s.isalpha()):
    print("String is alphabetic")
elif (s.isdigit()):
    print("String is digit")
elif (s.isalnum()):
    print("String is alpha and numeric")
elif (s.isspace()):
    print("string is space")
else:
    print("String is not alphabetic, numeric or both")
