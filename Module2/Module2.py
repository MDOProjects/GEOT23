if __name__ == '__main__':
    import Module2IO

def module2(weight, vac, flap, vmoWarn):
    
    #initialise variables
    vacWarn = 0 #Vertical acceleration warning
    manWarn = 0 #Manouvering Warning
    MaxTo = 115666 #Max takeoff weight (kg)
    MaxLnd = 95254 #Max landing weight (kg)
    up = 1
    takeoff = 2
    landing = 3
    flap_pos = up
    MaxG = 100
    
    #YOUR CODE HERE

        
    if(flap <= 0):#define flap positions
        flap_pos = up
    elif(flap <= 25):
        flap_pos = takeoff
    else:
        flap_pos = landing
           
    if (flap_pos == up):#vacWarn check for flaps up
        if(vac < -1):
            vacWarn = 1
        elif (vac > 2.5):
            vacWarn = 1
        else:
            vacWarn = 0
    if (flap_pos == takeoff): #vacWarn check for flaps in takeoff
        if(vac < 0):
            vacWarn = 1
        elif (vac >2):
            vacWarn = 1
        else:
            vacWarn = 0
    if (flap_pos == landing): #vacWarn check for flaps in landing
        if(weight > MaxTo):
            MaxG=1.5
        elif (weight <= MaxLnd):
            MaxG = 2
        else:
            MaxG = ((weight-176902)/-40824)
        if (vac > MaxG):
            vacWarn = 1
        else:
            vacWarn = 0
            
    if (vmoWarn & vacWarn):#manWarn control
        manWarn =1
    else:
        manWarn = 0
                        
    #Return outputs
    return vacWarn, manWarn
