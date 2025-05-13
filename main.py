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
    if numbers[i] > 0:
        first_index = i
        break
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_index = i
        break
for i in range(first_index + 1, last_index):
    sum += numbers[i]
print(sum, end=" ")'''
'''list = [2,3,4]
print(list)
list.append(6)
print(list)
list.clear()
print(list)'''
"""list = [2, 3, 4]
print('''выберите действие 1
выберите действие 2
выберите действие 3
4.показать список
5.количество элементов в списке
6.удаление с конкретных позиции
7.удаление конктретного элемента 
7.добавление конкретного элемента 
8.разворот в обратном порядке
9.сортировка списка
10.выход.''')
valid_check = True
while valid_check:
    check = int(input("выберите действие"))
    if check < 1 or check > 10:
        print("неккоректное значение")
    else:
        break
if check == 1:
    num1 = int(input("введите значение:"))
    list.sort()
elif check == 2:
    list.clear()
    print("список очищен")
elif check == 3:
    print(list)
elif check == 4:
    print("длина списка", len(list))
elif check == 5:
    index = int(input(''))
    if (index < 0 or index > len(list)):
        print("не существующий индекс")
    else:
        list.pop(index)
elif check == 6:
    try:
        list.remove(int(input("введите значение для удаления")))
    except:
        print("данное значение отсутствует")
elif check == 7:
    index = int(input(''))
    if (index < 0 or index > len(list)):
        print("не существующий индекс")
    else:
        num = int(input("введите значение"))
        list.insert(index, num)
elif check == 8:
    list.reverse()
    print("список развернут")
elif check == 9:
    list.sort()
    print("писок отсортирован")
elif check == 10:
    exit()
else:
    print("неккоректное значение"""


'''line="hbadlajhvlhvbdaljc sdlvabsd"
line2=" "
for i in line:
    line2=i+line2
print(line2)'''
'''ss="7 2 2 3 4 5 6 7"
ll=list(ss)
ll.reverse()
ss2=" "
for i in ll:
    ss2+=i
print(ss2)'''
'''line=input()
symbol=input()
print(line.count(symbol))'''
'''line=input()
symbol=input()
counter=0
for i in range'''
