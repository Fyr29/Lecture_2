# 1 Квадрат
square = int(input('Введите число, чтобы возвести его в квадрат: '))
square_result = square**2
print(f'{square} в квадрате = {square_result}')
print()


# 2 (1) Среднее арефметическое
average = list(input('Введите трех значное число: '))
average[0] = int(average[0])
average[1] = int(average[1])
average[2] = int(average[2])
average_result = int(average[0] + average[1] + average[2]) / 3
print(f'Среднее число из числел {average[0]}, {average[1]}, {average[2]} = {average_result}')
print()


# 2 (2) Среднее арефметическое
average_2 = int(input('Введите другое трех значное число: '))
average_x = average_2 // 100
average_y = average_2 % 100 // 10
average_n = average_2 % 10
# print(average_x, average_y, average_n)
average_result_2 = (average_x + average_y + average_n) / 3
print (f'А это среднее арифметическое из чисел {average_x}, {average_y}, {average_n} = {average_result_2}')
print()

# X // N = A
# A * N = Y
# X - Y = C
# X % N = C

# 3 Время
time = int(input('А сейчас минуты переведем в часы.\nПример: 270 = 4 часа 30 минут\nВведите число и мы посчитаем: '))
time_result_h = time // 60
time_result_m = time % 60
print(f'{time} минут = {time_result_h} часа(ов), {time_result_m} минут(ы)')
print()


# 4 Скидка
price = int(input('Теперь посчитаем скидку, введите цену товара: '))
discount = int(input('И введите скидку (%): '))
final_price = price * (1-discount / 100)
#price - (price * discount / 100)
print(f'Цена с учетом скидки составляет {final_price}')
print()


# 5 (Последняя цифра)
last = int(input('Введите любое число: '))
last_number = last % 10
print(f'Посдледняя цифра в вашем числе - {last_number}')
print()


# 6 (Периметр и площадь)
length = int(input('Посчитаем периметр и площадь.\nВведите длину: '))
width = int(input('Введите ширину: '))
perimeter = length * 2 + width * 2
area = length * width
print(f'Периметр = {perimeter}\nПлощадь = {area}')
print()


# 7 (1) (Столбик)
number = int(input('Введите 4-х значное число: '))
num_1 = number // 1000
num_2 = number % 1000 // 100
num_3 = number % 100 // 10
num_4 = number % 10
print(f'А вот столбик))\n{num_1}\n{num_2}\n{num_3}\n{num_4}')
print()

# X // N = A
# A * N = Y
# X - Y = C
# X % N = C

# 7 (2) (Столбик)
number_2 = list(input('введите другое 4-х значное число: '))
print(f'И второй столбик\n{number_2[0]}\n{number_2[1]}\n{number_2[2]}\n{number_2[3]}')


# echo "# education_python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Fyr29/Lecture_2.git
# git push -u origin main