class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = int(year)
    
    def info(self):
        print("Производитель -",self.brand)
        print("Модель -", self.model)
        print("Год выпуска -", self.year)

    def __del__(self):
        print("Сгорел сарай, сгорела хата")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed, pe):
        super().__init__(brand, model, year)
        self.fuel_type = int(fuel_type)
        self.max_speed = max_speed
        self.engine_capacity = int(engine_capacity)
        self.rotation_speed = int(rotation_speed)
        self.pe = int(pe)
    
    def info(self):
        super().info()
        print("Тип топлива -", self.fuel_type)
        print("Максимальная скорость -", self.max_speed,"км/ч")
        print("Объём двигателя", self.engine_capacity,"cм кубических")
        print("Частота вращения", self.rotation_speed,"об/мин")

    def engine_power_calc(self):
        if self.pe == 1:
            self.PE = 0,83
        elif self.pe == 2:
            self.PE = 0.9
        elif self.pe == 3:
            self.PE == 2
        self.e_power = self.engine_capacity * self.PE * (self.rotation_speed/120)
        print("Мощность двигателя =",self.e_power,"кВт")

    def __del__(self):
        print("Сгорел сарай, сгорела хата")


