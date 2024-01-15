from abc import ABC, abstractmethod
from engine import engine_service_check
from battery import battery_service_check


class Car(ABC):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        if engine_service_check(self.engine) or battery_service_check(self.battery):
            return True
        else:
            return False
        
