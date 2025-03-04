# Задача 1: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трёхзначное число: '))

sum = 0
c = 1
temp = 0

for i in range(number // 2):
    temp = number // c
    sum += temp % 10
    c *= 10

print(sum)