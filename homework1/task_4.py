# Задача 4: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = 3
m = 2
k = 4
# 6 4
if (n * m) % 2 == 0 and k % 2 == 0:
    print('yes')

elif (n * m) % 2 == 1 and k % 2 == 0:
    print('no')

elif (n * m) % 2 == 0 and k % 2 == 1:
    print('no')

elif (n * m) % 2 == 1 and k % 2 == 1:
    print('yes')
