class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = float(year)
    
    def info(self):
        print("Производитель -",self.brand)
        print("Модель -", self.model)
        print("Год выпуска -", self.year)

    def __del__(self):
        print("Сгорел сарай, сгорела хата")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed):
        super().__init__(brand, model, year)
        self.fuel_type = float(fuel_type)
        self.max_speed = max_speed
        self.engine_capacity = float(engine_capacity)
        self.rotation_speed = float(rotation_speed)
        self.pe = 1
    
    def info(self):
        super().info()
        print("Тип топлива -", self.fuel_type)
        print("Максимальная скорость -", self.max_speed,"км/ч")
        print("Объём двигателя", self.engine_capacity,"cм кубических")
        print("Частота вращения", self.rotation_speed,"об/мин")

    def engine_power_calc(self):
        if self.fuel_type == 1:
            self.pe = 0,83
        elif self.fuel_type == 2:
            self.pe = 0.9
        elif self.fuel_type == 3:
            self.pe == 2
        self.e_power = self.engine_capacity * self.pe * (self.rotation_speed/120)
        print("Мощность двигателя =",self.e_power,"кВт")

    def __del__(self):
        print("Сгорел сарай, сгорела хата")
