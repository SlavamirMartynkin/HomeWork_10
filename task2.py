# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input('Input a: '))
sum1 = a // 100 + (a // 10) % 10 + a % 10
print(sum1)
# или
b = input('Input b: ')
sum2 = (int(b[0]) + int(b[1]) + int(b[2]))
print(sum2)