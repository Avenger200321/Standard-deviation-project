import csv 
import math
with open('data.csv', newline='') as f:
    read = csv.reader(f)
    data = list(read)
data = data[0]
print(data)
n = len(data)
def mean(data):
    total = 0
    for i in data:
        total = total + int(i)
    mean = total/n
    return(mean) 
squaredList = []
for number in data :
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum + i 
result = sum/(n-1)
standard_deviation = math.sqrt(result)
print(standard_deviation)


