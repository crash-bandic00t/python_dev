import sys

# Длинное решение, если бы данные хранились построчно
if len(sys.argv) == 1:
    with open('sales.txt') as show:
        for line in show:
            print(line.strip())
elif len(sys.argv) == 2:
    line_cnt = 1
    with open('sales.txt') as show:
        line = show.readline().strip()
        while line:
            if line_cnt >= int(sys.argv[1]):
                print(line)
                line_cnt += 1
                line = show.readline().strip()
            else:
                line = show.readline().strip()
                line_cnt += 1
elif len(sys.argv) == 3:
    line_cnt = 1
    with open('sales.txt') as show:
        line = show.readline().strip()
        while line:
            if line_cnt >= int(sys.argv[1]) and line_cnt <= int(sys.argv[2]):
                print(line)
                line_cnt += 1
                line = show.readline().strip()
            else:
                line = show.readline().strip()
                line_cnt += 1