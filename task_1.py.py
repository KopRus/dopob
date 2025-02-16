
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строку формата, где марка и модель берутся с помощью атрибутов brand и model.
        >>> car = Car(brand='Toyota', model='Camry', year=2020)
        >>> str(car)
        'Toyota Camry'
        """
        return f'{self.brand} {self.model}'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.
        >>> car = Car(brand='Toyota', model='Camry', year=2020)
        >>> repr(car)
        'Car(brand='Toyota', model='Camry', year=2020)'
        """
        return f'Car(brand={self.brand!r}, model={self.model!r}, year={self.year})'


class Sedan(Car):
    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)
        self.doors = doors

    def __str__(self) -> str:
        """
        >>> sedan = Sedan(brand='Toyota', model='Camry', year=2020, doors=4)
        >>> str(sedan)
        'Toyota Camry'
        """
        return super().__str__()

    def __repr__(self) -> str:
        """
        >>> sedan = Sedan(brand='Toyota', model='Camry', year=2020, doors=4)
        >>> repr(sedan)
        'Sedan(brand='Toyota', model='Camry', year=2020, doors=4)'
        """
        return f'Sedan(brand={self.brand!r}, model={self.model!r}, year={self.year}, doors={self.doors})'


class Truck(Car):
    def __init__(self, brand: str, model: str, year: int, payload: float):
        super().__init__(brand, model, year)
        self.payload = payload

    def __str__(self) -> str:
        """
        >>> truck = Truck(brand='Ford', model='F-150', year=2020, payload=1.5)
        >>> str(truck)
        'Ford F-150'
        """
        return super().__str__()

    def __repr__(self) -> str:
        """
        >>> truck = Truck(brand='Ford', model='F-150', year=2020, payload=1.5)
        >>> repr(truck)
        'Truck(brand='Ford', model='F-150', year=2020, payload=1.5)'
        """
        return f'Truck(brand={self.brand!r}, model={self.model!r}, year={self.year}, payload={self.payload})'


if __name__ == "__main__":
    # Write your solution here
    pass


