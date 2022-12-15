from route import Route
from account_usser import User

class Trip:
    id          = int
    route       = Route
    user        = User("", "", "", "", "", "") 
    pago        = int
    progreso    = [int, int]
    
    def __init__(self,id, route, user, pago, progreso):
        self.id         = id
        self.route      = route
        self.user       = user
        self. pago      = pago
        self.progreso   = progreso