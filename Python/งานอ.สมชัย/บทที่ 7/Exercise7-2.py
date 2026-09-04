def check_palindrome(num):
    strNum = str(num)
    m = -1
    for n in range(len(strNum)//2):
        if (strNum[n] != strNum[m]):
            return False
        m = m - 1
    return True
print(check_palindrome(126621))