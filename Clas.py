class Car:
    def __init__(self, model, year, engine_volume, price, mileage):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4  # Количество колес по умолчанию для легкового автомобиля

    def description(self):
        return f"Модель: {self.model}\nГод выпуска: {self.year}\nОбъем двигателя: {self.engine_volume} л\nЦена: ${self.price}\nПробег: {self.mileage} км\nКоличество колес: {self.wheels}"


# Создаем экземпляр класса Car
car1 = Car("Toyota Camry", 2022, 2.5, 25000, 15000)

# Создаем класс-наследник Truck
class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8  # Количество колес для грузовика

# Создаем экземпляр класса Truck
truck1 = Truck("Volvo VNL", 2021, 12.8, 80000, 50000)

# Выводим информацию о легковом автомобиле и грузовике с помощью метода description
print("Информация о легковом автомобиле:")
print(car1.description())

print("\nИнформация о грузовике:")
print(truck1.description())
