first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print('Есть совпадение, результат = 3')
elif first == second or first == third or second == third:
    print('Есть совпадение, результат = 2')
else:
    print('Совпадений нет, результат = 0')