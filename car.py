from abc import ABC, abstractmethod
from engine import engine_service_check
from battery import battery_service_check


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
            
        
