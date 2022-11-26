#3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число!')
            
coordinate_x = give_int("Ведите координату Х точки А (любое число, кроме ноля):\n")
coordinate_y = give_int("Ведите координату Y точки А (любое число, кроме ноля):\n")
if coordinate_x != 0 and coordinate_y != 0:
    if coordinate_x > 0 and coordinate_y > 0:
        print(f'А({coordinate_x};{coordinate_y}) I-я четверть')
    if coordinate_x < 0 and coordinate_y > 0:
        print(f'А({coordinate_x};{coordinate_y}) II-я четверть')
    if coordinate_x < 0 and coordinate_y < 0:
        print(f'А({coordinate_x};{coordinate_y}) III-я четверть')
    if coordinate_x > 0 and coordinate_y < 0:
        print(f'А({coordinate_x};{coordinate_y}) IV-я четверть')     
else:       
    print ('Вы ввели ноль.')