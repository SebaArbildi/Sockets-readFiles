from TemperatureEntities import Temperature
import FileUtil
import os


if __name__ == '__main__':

    try:
        cityValues = FileUtil.FileUtil.readCityFile(os.path.realpath("../files/cityTempInpout.txt"))
    except Exception as e:
        raise e

    try:
        auxTemperature = Temperature.Temperature(cityValues["City"], int(cityValues["Temperature"]))
        cityInCelsius = Temperature.Temperature.convertFahrenheitToCelsius(auxTemperature)
    except Exception as e:
        raise e

    print("City:" + cityInCelsius.info()[0] + "Celsius Degrees:" + str(cityInCelsius.info()[1]))
    FileUtil.FileUtil.writeFile(os.path.realpath("../files/cityTempOutput.txt"), cityInCelsius.convertToDictionary())

