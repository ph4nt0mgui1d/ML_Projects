class book:
	def __init__(self, last, first, title, place, publisher, year):
		self.authorlast = last
		self.authorfirst = first
		self.title = title
		self.place = place
		self.publisher = publisher
		self.year = year

	def write_bib_entry(self):
		return self.authorlast + "," + self.authorfirst + "," + self.title + "," + self.place + "," + self.publisher + "," + str(self.year)

beauty = book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", 1999 )
pynut  = book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", 2003 )
print(beauty.write_bib_entry())
print(pynut.write_bib_entry())


# DONE