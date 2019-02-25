class Vehicle:
    def __init__(self, make, model, year, weight):

        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maitenance = False
        self.trips_since_maintenance = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_make):
        if type(new_make) == str:
            self.__make = new_make
        else:
            raise Exception('Invalid value for make')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if type(new_model) == str:
            self.__model = new_model
        else:
            raise Exception('Invalid value for model')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if type(new_year) == int:
            self.__year = new_year
        else:
            raise Exception('Invalid value for year')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if type(new_weight) == int:
            self.__weight = new_weight
        else:
            raise Exception('Invalid value for weight')

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maitenance = False
