# Create classes according to the following class-map:
# Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒ I am Dog. I am Pet. I am Animal

class Animal:

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Animal '

class Wild(Animal):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am wild {Animal.get_info(self)}'

class Leopard(Wild):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Leopard {Wild.get_info(self)}'

class Tiger(Wild):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Tiger {Wild.get_info(self)}' 

class pet(Animal):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am pet {Animal.get_info(self)}' 

class Dog(pet):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Dog {pet.get_info(self)}'

class Canine(Animal):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Canine {Animal.get_info(self)}'

class Fox(Canine):

    def get_name(self):
        return f'Hello..! My name is {self.name}.'

    def get_info(self):
        return f'I am Fox {Canine.get_info(self)}' 

obj = Tiger("Lion")
print(obj.get_name())
print(obj.get_info())

