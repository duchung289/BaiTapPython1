# Nong tai co 3 con ga, 3 con bo, 2 con cuu, tat ca cac con cung keu cung luc

#nong_trai=["ga1", "cuu2","ga2","cuu1","bo2","bo3","ga3","bo3"]
#nong_trai1=[ga[],cuu[],bo[]]
class Ga:
	def __init__(self, khoiluong, sotrung):
		self.khoiluong = khoiluong
		self.sotrung = sotrung

	def de(self):
		print("trung ga")

class Bo:
	def __init__(self, khoiluong, sanluong):
		self.khoiluong = khoiluong
		self.sanluong = sanluong
	def de(self):
		print("bo con")

class NongTrai:
	def __init__(self):
		self.chuong = [Ga(1, 10),Ga(1.3,11),Bo(90,5),Bo(95,7),Bo(89,6)]
		#self.chuong = [Ga(1, 10),Ga(1.3,11)]
	def sinhsan(self):
		for x in self.chuong:
			x.de()

nongtraiA = NongTrai()

nongtraiA.sinhsan()

		
