# Arbitrary arguments
def greet(*names):
    for name in names:
        print("Hello,", name)
        
greet("Harsh", "Pavan", "Aryan", "Muteen")      # it will keep expanding acc to the values you hv passed
