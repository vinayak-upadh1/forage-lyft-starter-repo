from car import Car 

class OctoprimeTyres(Car):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array
    
    def needs_service(self):
        return any(value>=3 for value in self.sensor_array) 