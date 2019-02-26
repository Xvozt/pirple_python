from vehicles import Vehicle


class Cars(Vehicle):
    """The Cars class. It inherits Vehicle class

    Arguments:
        Vehicle {object} --  vehicle class, with vehicle attributes
        such as: make, model, year, weight, how many trips
        are made since maitenance,
        does the car need new maitenance

    Returns:
        [object] -- instance of the cars class
    """
    __MAX_TRIPS_BEFORE_MAITENANCE = 100

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_driving = False

    def __closer_to_maitenance(self):
        """This method is called after the stop of the car
           Every stop closes the maitenance and after
           100 trips flag need_maitenance becomes true
        """
        self.trips_since_maintenance += 1
        if self.trips_since_maintenance > self.__MAX_TRIPS_BEFORE_MAITENANCE:
            self.needs_maitenance = True

    def drive(self):
        self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            self.__closer_to_maitenance()

    def __str__(self):
        return (self.make + ' ' + self.model + ' ' + str(self.year) + ' ' +
                str(self.weight) + ' ' + str(self.needs_maitenance) + ' ' +
                str(self.trips_since_maintenance))


def car_driving(car, trips_number):
    for dummy in range(trips_number):
        car.drive()
        car.stop()


# creating instances of Cars class
bmw = Cars('BMW', '3er', 2015, 1300)
audi = Cars('Audi', 'Q5', 2019, 2000)
alfa_romeo = Cars('Alfa Romeo', '4C', 2016, 1000)

# playing with attributes
print(bmw.model)
bmw.model = '2er'
audi.year = 2012
alfa_romeo.make = 'Fiat haha :)'


# car driving
car_driving(bmw, 150)
print(bmw)
bmw.repair()
print(bmw)

car_driving(audi, 101)
print(audi)

car_driving(alfa_romeo, 0)
print(alfa_romeo)
