from battery import nubbin_battery, spindler_battery
from engine import willoughby_engine, capulet_engine, sternman_engine
from car import Car 


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        car = Car(engine, battery)
        return car 
        
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = sternman_engine(warning_light_is_on)
        battery = spindler_battery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)
        car = Car(engine, battery)
        return car