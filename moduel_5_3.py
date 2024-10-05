class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors


    def go_to(self, new_floor):
        int(new_floor)
        for floor_number in range(1, new_floor+1):
            if new_floor < self.numbers_of_floors or new_floor < 1:
                print(floor_number)
            else:
                print('"Такого этажа не существует"')
                break

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей:{self.numbers_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors != other

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__