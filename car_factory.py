from battery import nubbin_battery, spindler_battery
from engine import willoughby_engine, capulet_engine, sternman_engine
from tyres import carrigan, octoprime
from car import Car 


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        tyres = carrigan(sensor_array)
        car = Car(engine, battery, tyres)
        return car 
        
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        tyres = carrigan(sensor_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, sensor_array):
        engine = sternman_engine(warning_light_is_on)
        battery = spindler_battery(current_date, last_service_date)
        tyres = carrigan(sensor_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        tyres = octoprime(sensor_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensor_array):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        tyres = octoprime(sensor_array)
        car = Car(engine, battery, tyres)
        return car