# Задание 2. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x=int(input('Введите значение x: '))
y=int(input('Введите значение y: '))
z=int(input('Введите значение z: '))
if (not (x or y or z) == (not x and not y and not z)):
    print(f'При x= {x}, y= {y}, z= {z} Выражение верно')
else:
    print('Выражение ложно')

# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
                
#                 if (not (x or y or z) == (not x and not y and not z)):
#                         print(f'x= {x}, y= {y}, z= {z} ')
#                 else:
#                     print(f'{x}, {y}, {z} False')