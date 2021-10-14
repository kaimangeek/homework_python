class Car():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Game():
    def __init__(self, length):
        self.length = length

    def play(self, n, cars):
        winners = []
        distance = n * self.length
        ds = [distance for _ in cars]
        while ds != [0] * len(ds):
            i = 0
            for car in cars:
                new_ds = ds[i] - car.speed
                if new_ds > 0:
                    ds[i] = new_ds
                else:
                    ds[i] = 0
                if ds[i] == 0 and not car.name in winners:
                    winners.append(car.name)
                i += 1
        print(winners)


car1 = Car("Mercedes", 5)
car2 = Car("BMW", 10)
car3 = Car("Lada", 1)
car4 = Car("Maclaren", 15)
car5 = Car("Tesla", 20)
g = Game(100)
print(g.play(5, [car1, car2, car3, car4, car5]))
