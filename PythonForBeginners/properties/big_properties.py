#big_properties.py
#By AdvaitThePro
class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
    @property
    def name(self):
        print("Sup Boi. \nNever mess with the pros.")
        return self.__name
    
    @name.setter
    def name(self, value):
        # cool validation here
        self.__name = value

presenter = Presenter("AdvaitThePro")
presenter.name = "AdvaitThePro"
print(presenter.name)