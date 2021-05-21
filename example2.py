class SomeClass:

    def __init__(self, name="Ozon_Express"):
        self.name = name


name_1 = SomeClass("Ozon_Travel")
name_2 = SomeClass()


def compare(first, second):
    return len(first) == len(second)


print(compare(name_1.name, name_2.name))
