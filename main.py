# 1 Квадрат
user_input_square = int(input('Введите число, чтобы возвести его в квадрат: '))
square_result = user_input_square**2
print(f'{user_input_square} в квадрате = {square_result}')
print()


# 2 (1) Среднее арефметическое
user_input_average = list(input('Введите трех значное число: '))
user_input_average[0] = int(user_input_average[0])
user_input_average[1] = int(user_input_average[1])
user_input_average[2] = int(user_input_average[2])
average_result = int(user_input_average[0] + user_input_average[1] + user_input_average[2]) / 3
print(f'Среднее число из числел {user_input_average[0]}, {user_input_average[1]}, {user_input_average[2]} = {average_result}')
print()


# 2 (2) Среднее арефметическое
user_input_average_2 = int(input('Введите другое трех значное число: '))
average_x = user_input_average_2 // 100
average_y = user_input_average_2 % 100 // 10
average_n = user_input_average_2 % 10
# print(average_x, average_y, average_n)
average_result_2 = (average_x + average_y + average_n) / 3
print (f'А это среднее арифметическое из чисел {average_x}, {average_y}, {average_n} = {average_result_2}')
print()

# X // N = A
# A * N = Y
# X - Y = C
# X % N = C

# 3 Время
user_input_time = int(input('А сейчас минуты переведем в часы.\nПример: 270 = 4 часа 30 минут\nВведите число и мы посчитаем: '))
time_result_h = user_input_time // 60
time_result_m = user_input_time % 60
print(f'{user_input_time} минут = {time_result_h} часа(ов), {time_result_m} минут(ы)')
print()


# 4 Скидка
user_input_price = int(input('Теперь посчитаем скидку, введите цену товара: '))
user_input_discount = int(input('И введите скидку (%): '))
final_price = user_input_price * (1-user_input_discount / 100)
#user_input_price - (user_input_price * user_input_discount / 100)
print(f'Цена с учетом скидки составляет {final_price}')
print()


# 5 (Последняя цифра)
user_input_last = int(input('Введите любое число: '))
last_number = user_input_last % 10
print(f'Посдледняя цифра в вашем чесле - {last_number}')
print()


# 6 (Периметр и площадь)
user_input_length = int(input('Посчитаем периметр и площадь.\nВведите длину: '))
user_input_width = int(input('Введите ширину: '))
perimeter = user_input_length * 2 + user_input_width * 2
area = user_input_length * user_input_width
print(f'Периметр = {perimeter}\nПлощадь = {area}')
print()


# 7 (1) (Столбик)
user_input_number = int(input('Введите 4-х значное число: '))
num_1 = user_input_number // 1000
num_2 = user_input_number % 1000 // 100
num_3 = user_input_number % 100 // 10
num_4 = user_input_number % 10
print(f'А вот слобик))\n{num_1}\n{num_2}\n{num_3}\n{num_4}')
print()

# X // N = A
# A * N = Y
# X - Y = C
# X % N = C

# 7 (2) (Столбик)
user_input_number_2 = list(input('введите другое 4-х значное число: '))
print(f'И второй столбик\n{user_input_number_2[0]}\n{user_input_number_2[1]}\n{user_input_number_2[2]}\n{user_input_number_2[3]}')


# echo "# education_python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Fyr29/Lecture_2.git
# git push -u origin main