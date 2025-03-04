# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input("Введите шестизначное число: "))

sum_of_first_numbers = 0
sum_of_last_numbers = 0
temp = 0
c = 1

for i in range (4):
    sum_of_last_numbers += temp % 10
    temp = number // c
    c *= 10

for j in range (4):
    sum_of_first_numbers += temp % 10
    temp = number // c
    c *= 10

print(f"Сумма первых трёх цифр в числе равняется: {sum_of_first_numbers}")
print(f"Сумма последних трёх цифр в числе равняется: {sum_of_last_numbers}")

if sum_of_first_numbers == sum_of_last_numbers:
    print('yes')
else:
    print('no')