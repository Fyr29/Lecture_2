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






# echo "# education_python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Fyr29/education_python.git
# git push -u origin main