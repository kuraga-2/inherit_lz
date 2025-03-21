from classs import Vehicle
from classs import Car
def main():
    a1 = input("Введите имя производителя - ")
    a2 = input("Введите модель - ")
    a3 = input("Введите год выпуска - ")
    choose = input("Это машина?\n Да/Нет\n")
    if choose == "Да":
        fuel = float(input("Если мотор бензиновый введите - 1 \nЕсли мотор форсированный введите - 2\nЕсли мотор дизельный введите - 3\nВаш выбор = "))
        max_speed = input("Введите макс скорость в км/ч - ")
        capacity = float(input("Введите объём двигателя в сантиметрах кубических - "))
        rot_speed = float(input("Введите частоту вращения в оборотах в минуту - "))
        vehiclee = Car(a1,a2,a3,fuel,max_speed,capacity,rot_speed)
        vehiclee.info()
        vehiclee.engine_power_calc()

    elif choose == "Нет":
        vehiclee = Vehicle(a1,a2,a3)
        vehiclee.info()
        
    else:
        print("Введите именно Да или Нет")

main()