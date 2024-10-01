global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    b = float(input("Высота: "))
    global result
    result = 0.5 * a * b

figure = input("1- прямоугольник, 2 - треугольник: ")
if (figure == '1'):
    rectangle()
elif (figure == '2'):
    triangle()
else:
    print("нет такого")

print(f"Площадь: {result}")