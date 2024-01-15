from car import Car 

class CarriganTyres(Car):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array
    
    def needs_service(self):
        return any(value>=0.9 for value in self.sensor_array) 