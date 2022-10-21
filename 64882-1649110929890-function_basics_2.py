def countDown(number):
    newList = []
    for i in range(number,-1,-1):
        newList.append(i)
    return newList



result = countDown(5)
print(result)

def printAndReturn(list):
    a = list[0]
    b = list[1]
    print(a)
    return b

printAndReturnOutcome = printAndReturn([1,2])
print(printAndReturnOutcome)

def firstPlusLength(list):
    sum = list[0] + len(list)
    return sum


firstPlusLengthOutcome = firstPlusLength([1,2,3,4,5])
print(firstPlusLengthOutcome)

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def this_length_that_value(a,b):
    output = []
    for i in range(0,a):
        output.append(b)
    return output

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))