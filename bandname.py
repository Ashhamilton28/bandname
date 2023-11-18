# Create a greeting for your program 
print("Welcome to Band Name Generator!")

# Ask user for city they grew up in 
city=input("What city did you grow up in? ").strip()

# Ask the user for the name of a pet 
pet_name=input("What is the name of your pet? ").strip()

# combine the name of their city and pet and show their band name 
band_name=(f"{city} {pet_name}")
print(f"Your band name is: {band_name}")
 