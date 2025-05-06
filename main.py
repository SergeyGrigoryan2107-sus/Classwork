'''students=["Иван","Олег","Виктор","Катя"]
students[2]="ttttt"
for i in range(len(students)):
    students[i]+="oooo"
    print(students[i])

for i in students:
    i+="1111"
    print(i)

print(students)'''
'''a=int(input("введите число"))
num=0
numbers=[0,1,2,3,4,5,6,7,8,9,87,1,2,32,1,6513,8,43,51,81,5,13,8,3,18,3,48]
for i in range(len(numbers)):
    if a==numbers[i]:
        num+=1
        print(num)'''
'''import random
numbers=[0,1,2,3,4,5,6,7,8,9,87,1,2,32,1,6513,8,43,51,81,5,13,8,3,18,3,48]
a=int(input("введите число"))
b=0

for i in range(a):
    print(numbers[random.randint(0,len(numbers)-1)], end=" ")'''
'''numbers=[0,1,2,3,4,5,6,7,8,9,87,1,2,32,1,6513,8,43,51,81,5,13,8,3,18,3,48]
a=len(numbers)-1
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i],end=" ")'''
'''numbers=[0,1,-2,3,5,-6,7,8,9,-87,1,2,-32,1,65,-13,8,-43,51,-81,5,-13,8,-3,-18,3,48]
sum1=0
for i in range(1,len(numbers)-1):
    if numbers[i]<0:
        sum1 += numbers[i]
print(sum1)'''
'''numbers=[0,1,-2,3,5,-6,7,8,9,-87,1,2,-32,1,65,-13,8,-43,51,-81,5,-13,8,-3,-18,3,48]
sum1=0
for i in range(0,len(numbers)-1):
    if numbers[i]%2==0:
        sum1 += numbers[i]
print(sum1,end=" ")'''
'''numbers=[0,1,-2,3,5,-6,7,8,9,-87,1,2,-32,1,65,-13,8,-43,51,-81,5,-13,8,-3,-18,3,48]
sum1=0
for i in range(1,len(numbers)-1):
    if numbers[i]%1==0:
        sum1 += numbers[i]
print(sum1)'''
'''numbers = [0, 1, -2, 3, 5, -6, 7, 8, 9, -87, 1, 2, -32, 1, 65, -13, 8, -43, 51, -81, 5, -13, 8, -3, -18, 3, 48]
sum_neg = 0
sum_odd = 0
sum_even = 0
for i in numbers:
    if i % 2 == 0:
        sum_odd += i
    else:
        sum_even += i
    if i < 0: sum_neg += i

for i in range(0, len(numbers), 3):
    print(numbers[i])'''
'''numbers = [0, 1, -2, 3, 5, -6, 7, 8, 9, -87, 1, 2, -32, 1, 65, -13, 8, -43, 51, -81, 5, -13, 8, -3, -18, 3, 48]
min = numbers[0]
max = numbers[0]
for i in range(0, len(numbers) - 1):
    if min > numbers[i]:
        min = numbers[i]
print(min,end=" ")
for i in range(0, len(numbers) - 1):
    if max < numbers[i]:
        max = numbers[i]
print(max,end=" ")'''
'''numbers = [0, 1, -2, 3, 65, -13, 8, -43, 51, -81, 5, -13, 8, -3, -18, 3, 48]
min = numbers[0]
max = numbers[0]
min_index = 0
max_index = 0
sum = 0
for i in range(0, len(numbers) - 1):
    if min > 0:
        min > numbers[i]
        min = numbers[i]
        min_index = i
print(min, end=" ")
for i in range(0, len(numbers) - 1):
    if max < numbers[i]:
        max = numbers[i]
        max_index = i
print(max, end=" ")
for i in range(min_index, max_index):
    sum += numbers[i]
print(sum, end=" ")'''
'''break'''
'''numbers = [0, 1, -2, 3, 65, -13, 8, -43, 51, -81, 5, -13, 8, -3, -18, 3, 48]
first_index = 0;
last_index = 0;
sum = 0
for i in range(0, len(numbers)):
    if numbers[i]> 0:
        first_index = i
        break
for i in range( len(numbers) - 1,-1,-1):
    if numbers[i]> 0:
        last_index = i
        break
for i in range(first_index+1, last_index):
    sum += numbers[i]
print(sum, end=" ")'''
