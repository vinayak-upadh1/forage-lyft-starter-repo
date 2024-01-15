from car import Car 

class OctoprimeTyres(Car):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array
    
    def needs_service(self):
        return sum(self.sensor_array)>=3 