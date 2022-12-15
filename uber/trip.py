from route import Route
from account_usser import User
from account_driver import Driver
from car import Car
from payment import Payment

class Trip:
    id          = int
    Car         = Car("", "", "", "", "")
    driver      = Driver("", "", "", "", "", "")
    user        = User("", "", "", "", "")
    route       = Route("", "", "", "")
    payment     = Payment("", "", "")
    
    def __init__(self, id, car, driver, user, route, payment):
        self.id         = id
        self.car        = car
        self.driver     = driver
        self.user       = user
        self. route     = route
        self.payment    = payment