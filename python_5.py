print("Physics Calculator")
a = int(input("Select a calculation:(1) Force (2) Energy (3) Power [enter the number]:"))
if a == 1:
    print("Force calculation selected.")
    mass = float(input("Enter mass (in kg): "))
    acceleration = float(input("Enter acceleration (in m/s^2): "))
    force = mass * acceleration
    print(f"The force is {force} N.")
elif a == 2:
    print("Energy calculation selected.")
    mass = float(input("Enter mass (in kg): "))
    height = float(input("Enter height (in meters): "))
    energy = mass * 9.81 * height
    print(f"The potential energy is {energy} J.") 
elif a == 3:
    print("Power calculation selected.")
    work = float(input("Enter work done (in joules): "))
    time = float(input("Enter time taken (in seconds): "))
    power = work / time
    print(f"The power is {power} W.")
else:
    print("Invalid selection. Please enter 1, 2, or 3.")