from vehicles import Vehicle


class Planes(Vehicle):
    __MAX_TRIPS_BEFORE_MAITENANCE = 100

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_flying = False

    def __closer_to_maitenance(self):
        """This method is called after the land of the plane
           Every stop closes the maitenance and after
           100 trips flag need_maitenance becomes true
        """
        self.trips_since_maintenance += 1
        if self.trips_since_maintenance > self.__MAX_TRIPS_BEFORE_MAITENANCE:
            self.needs_maitenance = True

    def fly(self):
        if self.needs_maitenance:
            print('The plane cannot fly, repair it!')
            return False
        else:
            self.is_flying = True
            return self.is_flying

    def land(self):
        if self.is_flying:
            self.is_flying = False
            self.__closer_to_maitenance()

    def __str__(self):
        return (self.make + ' ' + self.model + ' ' + str(self.year) + ' ' +
                str(self.weight) + ' ' + str(self.needs_maitenance) + ' ' +
                str(self.trips_since_maintenance))


def plane_flyer(plane, trips_number):
    for dummy in range(trips_number):
        if not plane.fly():
            break
        plane.land()

# creating an instance of Planes class
boeing = Planes('Boeing', '747', 1999, 10000)

# playing with attributes
boeing.make = 'Boeing_changed'
boeing.model = '737'
boeing.year = 2001
boeing.weight = 9000
# boeing.weight = '1000' - exception raised cause of check in setter

# lets fly
plane_flyer(boeing, 105)
print(boeing)
