# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = ''
        self._income =\
            {
                'wage': 1000,
                'bonus': 500
            }


class Position(Worker):

    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income['wage']+self._income['bonus']


a = Position()

print(a.get_full_name())
print(a.get_total_income())
