# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

while True:
    try:

        a = int(input('Введите число А: '))
        b = int(input('Введите число B: '))

        def Degree_Rec(x, y):
            if y == 0:
                return 1
            if y == 1:
                result = x
            else:
                result = x * Degree_Rec(x, y - 1)
            return result

        print(
            f'Результатом возвидения числа {a} в степень {b} явялется -> {Degree_Rec(a, b)}')
        break
    except:
        print('Ошибка! Необходимо ввести целое положительное число')
