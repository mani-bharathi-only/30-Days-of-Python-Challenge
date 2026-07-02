class Car:
    def __init__(self,name,color,year):
        self.name=name
        self.color=color
        self.year=year

    def start(self):
        print(f"Your started the {self.color} {self.name}")