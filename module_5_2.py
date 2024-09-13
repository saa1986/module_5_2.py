class House:
    def __init__(self, name, number_of_floors):  # Исправлено на __init__
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def display_info(self):  # Новый метод для отображения информации
        print(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __len__(self):  # Метод для получения количества этажей
        return self.number_of_floors

    def __str__(self):  # Метод для получения строкового представления объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вызов метода display_info для вывода информации
h1.display_info()
h2.display_info()

# Вывод количества этажей
print(len(h1))  # Используем метод __len__
print(len(h2))  # Используем метод __len__

# Вывод строкового представления объектов
print(h1)  # Используем метод __str__
print(h2)  # Используем метод __str__