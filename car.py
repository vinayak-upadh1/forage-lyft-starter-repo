from abc import ABC, abstractmethod
from engine import engine_service_check
from battery import battery_service_check


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return engine_service_check(self.engine) or battery_service_check(self.battery)
            
        
