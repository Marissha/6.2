class Vehicle:
    owner = str
    __model = str
    __engine_power = int
    __color = str

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def print_info(self):
        self.owner
        self.__model
        self.__color
        self.__engine_power
        print(f'Модель автомобиля: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец автомобиля: {self.owner}')

    def get_model(self):
        print(f'Модель автомобиля: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            print(f'автомобиль покрашен в {new_color}')
            self.__color = new_color
        else:
            print(f'автомобиль невозможно покрасить в {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()