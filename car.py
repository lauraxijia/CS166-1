
class Car:

 	def __init__(self, make, model, n_doors=5, year=2018, owner=None, mileage=0, pos=(0,0)):
 		self.make = str(make)
 		self.model = str(model)
 		self.n_doors = n_doors
 		self.year = year
 		self.owner = str(owner)
 		self.mileage = mileage
 		self.pos = pos

 	def drive(self, x, y):
 		self.pos = (self.pos[0]+x, self.pos[1]+y)
 		self.mileage += (x**2 + y**2)**.5

 	def sell(self, buyer):
 		self.owner = buyer

 	def __str__(self):
 		return self.make + " " + self.model + " (" + str(self.year) + ", " + str(self.mileage) + " miles)" 

c1 = Car("Audi", "A8")
c2 = Car("Mercedes", "E-Klasse")

c1.drive(10, 5)
print(c1)
print(c2)