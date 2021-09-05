# def main():
class radio:
	color = "Red"
	brand = "Sony"
	ACPower = True
	headphone = True
	
	def __init__(self):
		self.power_led = "ON"
		self.mode_led = "FM"
		self.frequency = 0.0
		self.volume = 10

	def power_switch(self, power_status):
		self.power_led = power_status
		print("Your radio is : " + str(self.power_led))

	def mode_switch(self, mode):
		self.mode_led = mode
		print("Your radio is set to : " + str(self.mode_led))

	def band_tuner(self, bandwidth):
		self.band_tuner = bandwidth
		print("Frequency is : " + str(self.band_tuner))

	def vol(self, volume):
		if(volume > 10 or volume < 0):
			return print("Invalid volume")
		self.volume = volume
		print("Volume is : " + str(self.volume))

my_radio = radio()
my_radio.power_switch("ON")
my_radio.band_tuner(108)
my_radio.vol(8)	

# if __name__ == "__main__":
# 	main()