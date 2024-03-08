
class Car:
    # Class Variable/Attribute
    serverUrl = "https://Organisation/CarConnect/Landing.asp"

    def __init__(self, make, model, year, color) -> None:
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0
        self._mileage = 0
        self._serial = Car.genSerial()

    # Static Method
    @staticmethod
    def genSerial():
        # Generates a serial number 
        # based on pattern and prev data
        return 10
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year
    
    @property
    def color(self):
        return self._color

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value
    
    @property
    def mileage(self):
        return self._mileage

    @property
    def serial(self):
        return self._serial
    
    def start(self):
        pass
    
    def __str__(self):
        return self.make + "--" + self.model + "--[" + str(self.speed) + "]--[" + str(self.serial) + "]"
    
    # Class Method
    @classmethod
    def serverurl(cls):
        return cls.serverUrl

def Test1():    
    car1 = Car("Toyota", "Camry", 2024, "Blue")
    print(car1.mileage())
    car1.Speed(40)
    print(car1)
    print(car1.make())

def Test2():
    car1 = Car("Toyota", "Camry", 2024, "Blue")
    print(car1.mileage)
    car1.Speed = 40
    print(car1)
    print(car1.make)

if __name__ == "__main__":
    # Test1()
    Test2()