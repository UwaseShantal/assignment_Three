####Car assembly factory called Akatsuki heavy industries for different catergories of vehicles which include domestic and military and what is required depending on the type of vehicle
###This is a program to show where different vehicles will be transferred depending on the catergory type and the benefits the vehicle offers
###This program will give the user choices between domestic and military vehicles
###if domsetic is select another set of choices which are for types of cars which include Sedans, Hatchbacks and Vans
###if a sedan is selected then only wheels are to be added and the vehicle wheel size should be less than 16
###if hatchback is selected then a body kit is to be selected 
###if family vehicles are selected they are to be transferred to family vehicle sales
###Under the military vehicle catergory there are different grades of armour under which are to be tested. If the vehicles pass the test they are to be sent to designated areas if the fail they are to be sent back to the factory
##Welcome user
print("Welcome to Akatsuki heavy industries")

#Give the user choices of vehicle catergory either Domestic or Military
print("Stage 1")
print("1:Domestic")
print("2:Military")
#Ask user to input a number represnt the vehicle catergory
type=int(input("Select a category of vehicle:"))

#Incase domestic  type is selected give user a different set of choices relating to the type of domestic vehicle
if type==1:
    print("Proceed. Which category of vehicle is it?")
    print("1:Sedan")
    print("2:Hatchback")
    print("3:Van")
    #ask for a domestic vehicle type
    dom=int(input("Select a domestic vehicle type: "))
    
    ##First nested if
    #Selection of sedan under domestic vehicles
    if dom==1:
        #Ask user to select a wheel size
        wheel=int(input("Select a wheel size: "))
        
        ##Nested if under sedan selection dealing with wheel size
        #if wheel size is greater than 16 give user a warning
        if wheel>=16:
            print("WARNING!! The wheel size will lower car's center of gravity are you sure")
        else:
            print("Transfer vehicle to sedan sales department")    
   
    #Selection of hatchback body kits under domestic vehicles(elif since more than to choices are present)
    elif dom==2: 
        print("Available body kits")
        print("1:Stock")  
        print("2:Aerodynamic")
        print("3:Wide")
       
        #Ask user to select a body kit
        kit=int(input("Select a body kit: "))
       
        ##Nested if under hatchback selection for body kits
        #when the user enters "1" the code should output a phrase to transfer to general sales
        if kit==1:
            print("Transfer to  hatchback general sales ")
        #For the first elif condition when the user enters "2" the code should output a phrase to transfer to endurance racing sales
        elif kit==2:
            print("Transfer to hatchback endurance racing sales ")   
        #For the second elif condition when the user enters "3" the code should ouput a phrase to transfer to offroad sales department
        elif kit==3:
            print("Transfer to offroad sales department")  
        #Else condition to give user feedback incase they enter any other feedback
        else:
            print("Sorry no kit aside from the above kits exists")     
    
    #Selection for family vehicles will use else condition(elif refuse to work )
    else:
        print("Send to the family cars section")     
else:
    #armoured vehicle
    #input type of armour plating
    print("Select an armour plating")        
    print("1:B4")
    print("2:B5")
    print("3:B6")
    arm=int(input("Select an armour plating category"))
    
    ##Nested if to deal with the category selected
    #Incase a category "1" is selected the code should should print out "To be sent to handgun testing"
    if arm==1:
        #handgun testing
        print("To be sent to handgun testing")
        print("1:Yes")
        print("2:No")
        handgun_testing=int(input("Did the vehicle pass the test: "))
        
        ##Nested if for result of handgun testing
        #if user enters "1" this means the vehicle passed handgun testing, transfer to government garage
        if handgun_testing==1:
            print("Transfer to government garage")
        #if user enters "2" this means that it has failed so it is to be returned to assemblig factory
        else:
            print("Return to assembling facility")    
    #nested elif condition under armoured vehicle (assualt rifle testing)
    elif arm==2:
        print("To be sent to assault rifle testing")
        print("1:Yes")
        print("2:No")
        handgun_testing=int(input("Did the vehicle pass the test: "))
       
        ##nested if for results of assault rifle testing
        #if user enters "1" that means the code should output transfer to government garage main
        if handgun_testing==1:
            print("Transfer to government garage main")
        #Incase user enters "2" meaning it has failed testing the code should output "Return to assembling facility"
        else:
            print("Return to assembling facility")    
    # else of nested if condition under armoured vehicle (shotgun testing)
    else:
        print("To be sent to shotgun testing")  
        print("1:Yes")
        print("2:No")
        handgun_testing=int(input("Did the vehicle pass the test: "))
        
        ##nested if for results of shotgun testing
        #if user enters "1" that means the code should output transfer to military base
        if handgun_testing==1:
            print("Transfer to  military base")
        else:
           print("Return to assembling facility")   




