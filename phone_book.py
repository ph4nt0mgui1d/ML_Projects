import re

fh = open("simpsons_phone_book.txt", 'r')

for line in fh:
	if(re.search(r'^J\w*\s*(Neu)', line)):
		print(line)

fh.close()