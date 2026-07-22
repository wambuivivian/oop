class Vehicle:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"the engine of the {self.year} {self.make} {self. model}is stoping"
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"vihicle(make='{self.make}', model='{self.model}', year={self.year})"
