from battery import nubbin_battery, spindler_battery
import datetime


def needs_service(battery_name):
    if battery_name=='nubbin':
        battery = nubbin_battery(datetime.datetime.now())
        if battery.needs_service():
            return True
        return False
    else:
        battery = spindler_battery(datetime.datetime.now())
        if battery.needs_service():
            return True
        return False
        