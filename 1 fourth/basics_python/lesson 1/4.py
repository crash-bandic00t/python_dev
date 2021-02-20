for i in range(101):
    num = str(i)
    if num[-1] == '0'  or num[-1] == '5' or num[-1] == '6' or num[-1] == '7' or num[-1] == '8' or num[-1] == '9':
        print(f'{i} процентов')
    elif num[-1] == '2' or num[-1] == '3' or num[-1] == '4':
        print(f'{i} процента')
    elif num[-1] == '1':
        print(f'{i} процент')