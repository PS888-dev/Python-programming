def find_max(num):
    max = 0
    while num > 0:
        digit = num % 10
        if (digit > max):
            max = digit
        num = num // 10
    return(max)


    # max_digit=0
    # for i in str(num):
    #     if int(i) > max_digit:
    #         max_digit=int(i)
    # return(max_digit)

print(find_max(12345))