import math

def module1(pitot, stat, rho, VACLimit):
    
    #initialise variables
	kias = 0
	vmo = 500
	vmoWarn = 0
	
	#Calculate Vmo
	vmo = 500 if VACLimit > 2.0 else VACLimit*500 - 600
	vmo = 150 if VACLimit < 1.5 else vmo
	
	#Calculate airspeed
	kias = math.sqrt(6894.76*(pitot - stat)/rho)*1.94384 if pitot > stat else -1;
	
	#Set warning flag on/off
	vmoWarn = 1 if kias > vmo else 0
	
	#Return outputs
	return kias, vmoWarn, vmo
