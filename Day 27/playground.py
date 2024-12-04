
def add(*args):
    return sum(args)

print(add(4, 5, 6, 7, 5, 67, 78, 8))


def calculate(n, **kwargs):
    print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

car = Car(make="Nissan")
print(car.make, car.model)