# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from Animals.Bird import Bird
from Animals.Fish import Fish


class Factory:
    def __init__(self, type_class, *args):
        self.type_class = type_class
        self.args = args

    def return_class(self):
        return self.type_class(*self.args)

    def __str__(self):
        return f'type_class: {self.type_class}, args: {self.args}'


if __name__ == '__main__':
    a = Factory(Fish, 'Fi', 'ocean')
    print(a)
    print(a.return_class())
    b = Factory(Bird, 'Bi', 20, 'red')
    print(b.return_class())
