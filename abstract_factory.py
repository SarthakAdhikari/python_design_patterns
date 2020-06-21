from abc import ABC, abstractmethod


class AbstractChair(ABC):
    @abstractmethod
    def sitOn() -> str:
        pass

    @abstractmethod
    def hasLegs() -> bool:
        pass


class AbstractTable(ABC):
    @abstractmethod
    def open_drawer() -> str:
        pass

    @abstractmethod
    def close_drawer() -> str:
        pass


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(color="white") -> AbstractChair:
        pass

    @abstractmethod
    def create_table(color="brown") -> AbstractTable:
        pass


class VictorianFurniture(AbstractFurnitureFactory):
    def __init__(self, color):
        self.color = color

    def create_chair(self):
        return VictorianChairFactory(self.color)

    def create_table(self):
        return VictorianTableFactory(self.color)


class ModernFurniture(AbstractFurnitureFactory):
    def __init__(self, color):
        self.color = color

    def create_chair(self):
        return ModernChairFactory(self.color)

    def create_table(self):
        return ModernTableFactory(self.color)


class VictorianChairFactory:
    def __init__(self, color):
        self.color = color

    def sitOn(self):
        return "Sat on a {} Victorian Chair.".format(self.color)

    def has_legs(self):
        return True


class VictorianTableFactory:
    def __init__(self, color):
        self.color = color

    def open_drawer(self):
        return "{} colored Victorian drawer opened.".format(self.color)

    def close_drawer(self):
        return "{} colored Victorian drawer closed.".format(self.color)


class ModernChairFactory:
    def __init__(self, color):
        self.color = color

    def sitOn(self):
        return "Sat on a {} modern Chair.".format(self.color)

    def has_legs(self):
        return False


class ModernTableFactory:
    def __init__(self, color):
        self.color = color

    def open_drawer(self):
        return "{} colored Modern drawer opened.".format(self.color)

    def close_drawer(self):
        return "{} colored Modern drawer closed.".format(self.color)


def client_code(factory: AbstractFurnitureFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()

    print(chair.sitOn())
    print("Chair has legs? ", chair.has_legs())

    print(table.open_drawer())
    print(table.close_drawer())


if __name__ == "__main__":
    # For Victorian furnitures
    print("*" * 10)
    print("For Victorian Furnitures")
    print("*" * 10)
    client_code(VictorianFurniture("Red"))

    # For Victorian furnitures
    print("*" * 10)
    print("For Modern Furnitures")
    print("*" * 10)
    client_code(ModernFurniture("Black"))
