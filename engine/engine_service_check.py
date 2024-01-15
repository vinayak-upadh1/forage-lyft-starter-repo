from engine import capulet_engine, sternman_engine, willoughby_engine

def needs_service(engine_name):
    if engine_name=='capulet':
        engine = capulet_engine(current_mileage, last_service_mileage)
        if engine.engine_should_be_serviced():
            return True
        return False

    elif engine_name=='sternman':
        engine = sternman_engine(warning_light_is_on)
        if engine.engine_should_be_serviced():
            return True
        return False
    
    else:
        engine = willoughby_engine(current_mileage, last_service_mileage)
        if engine.engine_should_be_serviced():
            return True
        return False
        
    
        