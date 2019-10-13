
#starters1=[['TORTILA',4.5],['olivas',4.00],['GAMBAS',5.5]]

#starters1.sort(key=lambda x: x[1])
#print(starters1)

#TODO: need to lear more about
class Menu:
	def __init__(self, name, price):
		self.name = name
		self.price = price
	def __repr__(self):
		return "{} {}".format(self.name, self.price)

starters1 = [Menu("TORTILA",4.5), Menu('olivas',4.0), Menu('GAMBAS',5.5)]

starters1.sort(key=lambda x: x.name)

print(starters1)