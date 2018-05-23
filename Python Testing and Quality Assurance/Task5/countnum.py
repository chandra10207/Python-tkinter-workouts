def countNum(start, end, num):
    count = 0
    for i in range(start, end+1):
        if str(num) in str(i):
            count = count + 1
    return count


