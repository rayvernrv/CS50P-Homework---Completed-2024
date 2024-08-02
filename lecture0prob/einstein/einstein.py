#Ask user to key in the mass for E=mc^2 calc
mass=int(input ("What's the mass in kg? "))

# Assume c is 300000000 meters per second
E=mass*300000000**2  # ** means power of
print (f"{E:,}")
