#Task 1 
def device_range(device):
    """Receives device name and returns the normal range of energy consumption."""
    device=device.lower()

    if device=="led light":
        return 0.01,0.10
    elif device=="television":
        return 0.05,0.50
    elif device=="refrigerator":
        return 0.10,1.50
    elif device=="washing machine":
        return 0.30,2.50
    elif device=="air conditioner":
        return 0.50,5.00
    else:
        return 0,0

#1.2
def energy_status(device,energy):
    """Receives device name & energy consumption and returns status of device."""
    minimum,maxinum= device_range(device)

    if minimum==0 and maxinum==0:
        return "Unknown device name."
    elif energy<0:
        return "Energy cannot be negetive"
    elif energy<minimum:
        return "Low"
    elif energy>=minimum and energy<maxinum:
        return "Normal"
    elif energy>=maxinum and energy<(maxinum*2):
        return "High"
    elif energy>=(maxinum*2):
        return "Critical"
    else:
        return "Error"

# 1.3
def requires_attention(device,energy):
    """Determines whether a device needs attention. Recieves device name and energy consumption
    and returns True if attention is needed or else returns false"""

    status=energy_status(device,energy)
    if status=="High" or status=="Critical":
      return True
    elif status=="Normal":
      return False
    else:
        return "Status is not valid."

# Task 2 
def calculate_cost(energy,rate):
    """Receives energy consumption & rate of electricity and returns the estimated cost of electricity"""

    if energy<0 or rate<0:
        return "Energy or Rate cannot be negetive values."
    
    cost=energy*rate
    return cost

# Task 3
def feedback(device,energy):
    """Receives device name & energy consumption and returns feedback of device according to status"""

    status=energy_status(device,energy)
    if status=="Unknown device name.":
        return "Status is not valid."
    
    device=device.lower()
    status=status.lower()
    print("Device: ",device)
    print("Energy: ",energy)
    print("Status: ",status)

    if device=="led light":

        if status=="normal":
            if energy>=0.01 and energy<0.10:
                return "Energy consumption of device is normal. Continue normal usage"
            else:
                return "Incorrect status reading"
        elif status=="high":
            if energy>=0.10 and energy<0.20:
                return "Slightly high energy consumption. Observe energy consumption of device." 
            else:
                return "Incorrect status reading"
        elif status=="critical":
            if energy>=0.20:
                return "Very high energy status. Lower energy consumption of device immediately"
            else:
                return "Incorrect status reading"
        else:
            return "Incorrect status reading"

    elif device=="television":

        if status=="normal":
            if energy>=0.05 and energy<0.50:
                return "Energy consumption of device is normal. Continue normal usage"
            else:
                return "Incorrect status reading"
        elif status=="high":
            if energy>=0.50 and energy<1.00:
                return "Slightly high energy consumption. Observe energy consumption of device."  
            else:
                return "Incorrect status reading"
        elif status=="critical":
            if energy>=1.00:
                return "Very high energy status. Lower energy consumption of device immediately"
            else:
                return "Incorrect status reading"
        else:
            return "Incorrect status reading"

    elif device=="refrigerator":

        if status=="normal":
            if energy>=0.10 and energy<1.50:
                return "Energy consumption of device is normal. Continue normal usage"
            else:
                return "Incorrect status reading"
        elif status=="high":
            if energy>=1.50 and energy<3.00:
                return "Slightly high energy consumption. Observe energy consumption of device."  
            else:
                return "Incorrect status reading"
        elif status=="critical":
            if energy>=3.00:
                return "Very high energy status. Lower energy consumption of device immediately"
            else:
                return "Incorrect status reading"
        else:
            return "Incorrect status reading"

    elif device=="washing machine":

        if status=="normal":
            if energy>=0.30 and energy<2.50:
                return "Energy consumption of device is normal. Continue normal usage"
            else:
                return "Incorrect status reading"
        elif status=="high":
            if energy>=2.50 and energy<5.00:
                return "Slightly high energy consumption. Observe energy consumption of device."
            else:
                return "Incorrect status reading"
        elif status=="critical":
            if energy>=5.00:
                return "Very high energy status. Lower energy consumption of device immediately"
            else:
                return "Incorrect status reading"
        else:
            return "Incorrect status reading"

    elif device=="air conditioner":

        if status=="normal":
            if energy>=0.50 and energy<5.00:
                return "Energy consumption of device is normal. Continue normal usage"
            else:
                return "Incorrect status reading"
        elif status=="high":
            if energy>=5.00 and energy<10.0:
                return "Slightly high energy consumption. Observe energy consumption of device."
            else:
                return "Incorrect status reading"
        elif status=="critical":
            if energy>=10.0:
                return "Very high energy status. Lower energy consumption of device immediately"
            else:
                return "Incorrect status reading"
        else:
            return "Incorrect status reading"

    else:
        return "Device not found. Please try again"


#Task 4 and 5
def all_readings():
    """Reads all the data in for loop and returns all data required for homesense report"""
    total_readings=0
    normal_readings=0
    high_readings=0
    critical_readings=0
    readings_attention=0
    total_energy=0
    total_cost=0
    highest_energy=0
    highest_device=""

    try:
        rate=float(input("Enter the Energy consumption rate per kWh: "))
        if rate<0:
            print("Rate cannot be negative value.")
            return
    except ValueError :
        print("Please enter number only")
        return
    
    for i in range (1,11):
        total_readings=total_readings+1

        if i==1:
            device="LED Light"
            energy=0.06
        elif i==2:
            device="LED Light"
            energy=0.18
        elif i==3:
            device="Television"
            energy=0.32
        elif i==4:
            device="Television"
            energy=1.20
        elif i==5:
            device="Refrigerator"
            energy=0.80
        elif i==6:
            device="Refrigerator"
            energy=2.20
        elif i==7:
            device="Washing Machine"
            energy=1.40            
        elif i==8:
            device="Washing Machine"
            energy=4.50
        elif i==9:
            device="Air Conditioner"
            energy=2.80
        elif i==10:
            device="Air Conditioner"
            energy=7.50
        
        if energy>highest_energy:
            highest_energy=energy
            highest_device=device

        # Gets status from another def function
        stat=energy_status(device,energy)

        if stat=="Normal":
            normal_readings=normal_readings+1
        elif stat=="High":
            high_readings=high_readings+1
        elif stat=="Critical":
            critical_readings=critical_readings+1
        else:
            print("Error")

        # Gets attention status from another def function
        attention=requires_attention(device,energy)
        if attention==True:
            readings_attention=readings_attention+1

        # Gets total cost calculation from another def function
        cost=calculate_cost(energy,rate)

        total_energy=total_energy+energy
        total_cost=total_cost+cost

    report(total_readings,normal_readings,high_readings,critical_readings,readings_attention,total_energy,total_cost,highest_device,highest_energy)

# Task 6
def report(total_readings,normal_count,high_count,critical_count,attention_count,total_energy,total_cost,highest_device,highest_energy):
    """Receives all reading informations and prints a homesense report according to reading."""

    print("========== HomeSense Report ==========")
    print("Readings analyzed: ",total_readings)
    print()
    print("Normal: ",normal_count)
    print("High: ",high_count)
    print("Critical: ",critical_count)
    print()
    print("Readings requiring attention:",attention_count)
    print()
    print("Total energy: ",total_energy,"kWh")
    print("Estimated cost: AED",total_cost)
    print()
    print("Highest consumption device: ",highest_device)
    print("Highest energy consumption: ",highest_energy)

# testing

print("======== Device Range Output ========")
print("LED Light range: ",device_range("LED Light"))
print("Air Conditioner range: ",device_range("aiR CoNDiTionEr"))
print("Unknown device range: ",device_range("Laptop"))
print("")

print("======== Device Status Output ========")
print("Television: ",energy_status("Television",0.50))
print("Television: ",energy_status("TelevIsion",0.05))
print("Refrigerator: ",energy_status("refrigerator",0.000001))
print("LED light: ",energy_status("led light",1.0001))
print("LED light: ",energy_status("Led light",0))
print("Negative energy: ",energy_status("LED Light",-2.00))
print("Random device: ",energy_status("Computer",0.80))
print("")

print("======== Boolean Output Of Status ========")
print("Attention required for normal: ",requires_attention("Television",0.32))
print("Attention required for high: ",requires_attention("Television",0.71))
print("Unknown device: ",requires_attention("Televisi",2.90))
print("")

print("======== Output Of Total Energy Cost ========")
print("Normal cost: ",calculate_cost(4.2,0.49))
print("Zero energy cost: ",calculate_cost(0,0.20))
print("Negative energy: ",calculate_cost(-2.9,0.30))
print("")

print("======== Output Of different feedbacks ========")
print("LED light normal feedback: ",feedback("Led light",0.06))
print("LED light high feedback: ",feedback("Led light",0.15))
print("LED light critical feedback: ",feedback("Led light",0.26))
print("Unknown device feedback: ",feedback("Light",0.90))
print("")

print("======== Output Of HomeSense Report Of All Readings ========")
print("")
all_readings()

