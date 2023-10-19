from abc import ABC


class Gari:
    def mileage(self):
        pass


class Toyota(Gari):
    def mileage(self):
        print("My mileage is 300kmph")


class Nissan(Gari):
    def mileage(self):
        print("My mileage is 400kmph")
