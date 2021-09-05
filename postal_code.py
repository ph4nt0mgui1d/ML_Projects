import re

largest_cities_file = open("largest_cities_germany.txt", 'r')
largest_cities_data = largest_cities_file.readlines()

regex_cities = re.compile(r'\s[\w\s]+\s+')   #have to figure out the regex
city_names = []

for city_data in largest_cities_data:
	city_name = regex_cities.findall(city_data)[0]    #[0] is used to take the first occurence i.e. at first index.
	city_names.append(city_name.strip())			# strip method is used to remove leading and trailing spaces.

postal_datafile = open("postal_codes_germany.txt", 'r')
postal_data = postal_datafile.read()

result = {}

for name in city_names:
	reg_exp = '\s'+name+'\s[\d]+\s'				#+name+ is the syntax to add a variable in regex
	city_matches = (re.findall(reg_exp,postal_data)[0:3])		#[0:3] for only 3 entries
	city_matches_str = "".join(city_matches)				#join method used to concatenate any number of strings. 

	result[name] = re.findall(r'[0-9]+', city_matches_str)

print(result)