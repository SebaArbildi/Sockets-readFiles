from TemperatureEntities import TemperatureType


class Temperature:
    def __init__(self, city, value):
        self.__set__city(city)
        self.__set__value(value)

    def __get__value(self):
        return self.__value

    def __set__value(self, value):
        if isinstance(value, (int, float)):
            self.__value = value
        else:
            raise TypeError("Type must be a int or a float")

    def __get__city(self):
        return self.__city

    def __set__city(self, city):
        if isinstance(city, str):
            self.__city = city
        else:
            raise TypeError("Type must be a int or a float")

    def info(self):
        return self.__get__city(), self.__get__value()

    def convertToDictionary(self):
        return {"City": self.__get__city(), "Temperature": self.__get__value()}

    @classmethod
    def convertFahrenheitToCelsius(cls, temperature):
        if isinstance(temperature, Temperature):
            celsiusValue = (temperature.__get__value() - 32) * (5 / 9)
            celsius = cls(temperature.__get__city(), int(round(celsiusValue)))
            return celsius
        else:
            raise TypeError("Type must be a Temperature")



'''
    @classmethod
    def convertCelsiusToFahrenheit(cls, celsius):
        if isinstance(celsius, Temperature):
            fahrenheitValue = (celsius.value * (9 / 5)) + 32
            fahrenheit = cls(TemperatureType.TemperatureType.Fahrenheit, int(round(fahrenheitValue)))
            return fahrenheit
        else:
            raise TypeError("Type must be a int or a float")

    def __get__tempType(self):
        return self.tempType

    def __set__tempType(self, tempType):
        if isinstance(tempType, TemperatureType.TemperatureType):
            self.tempType = tempType
        else:
            raise TypeError("Type must be a TemperatureType")
'''