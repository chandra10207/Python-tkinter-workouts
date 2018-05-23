def countNum(start, end, num):
    count = 0
    for i in range(start, end+1):
        if str(num) in str(i):
            count = count + 1
    return count

print(countNum(1,5,8))
print(countNum(1,500,2))
print(countNum(-50,-5,6))
print(countNum(100,1000,42))
print(countNum(1,12,1))
print(countNum(5,5,5))


