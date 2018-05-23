def countNum(start, end, num):
    count = 0
    if(type(start) is not int or type(end) is not int or type(num) is not int):
        return "TypeError" 
    elif(start > end):
        return "ValueError"
    
    elif(num < start or num > end):
        return "ValueError"        
        
    else:
        for i in range(start, end+1):
            if str(num) in str(i):
                count = count + 1
        return count

print(countNum(1.5,9,5))
print(countNum(1,9.5,5))
print(countNum(1,9,5.5))
print(countNum('A',9,5))
print(countNum(9,1,5))
print(countNum(1,9,-5))


