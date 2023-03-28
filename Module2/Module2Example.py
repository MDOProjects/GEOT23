if __name__ == '__main__':
    import Module2IO

def module2(weight, vac, flap, vmoWarn):
    
    #initialise variables
    vacWarn = 0
    manWarn = 0
    
    #Establish weight bounds
    TakeoffW = 115892
    LandW = 95254
    
    #Clamp weight to bounds
    weight = TakeoffW if weight > TakeoffW else weight
    weight = LandW if weight < LandW else weight
    
    #Calculate VAC Limits
    VACLimit = 2.0 if flap > 0 else 2.5
    VACLimit = (-0.5 *(weight - LandW)/(TakeoffW - LandW) + 2) if flap > 20 else 2.0
    nVACLimit = 0.0 if flap > 0 else -1.0
    
    #Set warnings flag on/off
    vacWarn = 1 if vac > VACLimit or vac < nVACLimit else 0
    manWarn = 1 if vacWarn and vmoWarn else 0
	
    #Return outputs
    return vacWarn, manWarn
