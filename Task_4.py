# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

#Пример:
# quarter = 1 = x∈(0, ∞) u y∈(0,∞)
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Вы ввели не число! ПОПРОБУЙТЕ ЕЩЕ РАЗ. ')
            
number_quarter = give_int("Ведите номер четверти (число от 1 до 4):\n")
if number_quarter >=1 and number_quarter <=4:
    if number_quarter == 1:
        print('I-я четверть. X ∈ (0; +∞) и Y ∈ (0; +∞)')
    if number_quarter == 2:
        print('II-я четверть. X ∈ (0; -∞) и Y ∈ (0; +∞)')
    if number_quarter == 3:
        print('III-я четверть. X ∈ (0; -∞) и Y ∈ (0; -∞)')
    if number_quarter == 4:
        print('IV-я четверть. X ∈ (0; +∞) и Y ∈ (0; -∞)')    
else:       
    print ('Вы ввели некорректное число!')