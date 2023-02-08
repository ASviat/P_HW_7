# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self):
        self.speed = 220
        self.color = 'black'
        self.name = 'Honda'
        self.is_police = False

    def go(self):
        print('Машина в движении.')

    def stop(self):
        print('Машина остановилась. ')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self, speed):
        if speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    pass


wc = WorkCar()
c = Car()
print(wc.show_speed(60))
print(c.show_speed())
c.go()
c.turn('налево.')
sc = SportCar()
sc.stop()
