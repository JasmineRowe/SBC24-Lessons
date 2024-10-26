

class Musician: 
    def __init__(self, name, instrument):

        self.name = name
        self.instrument = instrument


        
    # Define a method named musician_name that belongs to the Musician class
    def musician_name(self):
        # This method returns a string that says the musician is a musician 
        return f"{self.name} is a musician"
    
    # Define a method named `get_instrument` that returns the dog's age
    def get_instrument(self):
        # This method returns a string with the dog's name and age
        return f"{self.name} plays the {self.instrument}" 
    
    

    # 2. Creating Objects
# Instantiate (create) objects of the Musician class with specific attributes

# Create an object named `dog1` with the name "Buddy" and age 3
musician1 = Musician("Jasmine Rowe", "guitar")
# Create another object named `dog2` with the name "Max" and age 5
musician2 = Musician("Ollie Hutton", "keys")
# Print details for `dog2`

# Call the `get_age` method for `dog2` and print the result
print(musician1.musician_name())  # Output: Jasmine Rowe is a musician
# Call the `bark` method for `dog2` and print the result
print(musician2.get_instrument())     # Output: Ollie Hutton plays the keys
