
# ============================================================
# Exercise 2: Dogs
# Instructions:
# Create a Dog class with bark() and jump() methods.
# Instantiate dog objects, call their methods and compare sizes.
#
# Step 1: Create a Dog class with name and height attributes.
#         - bark() prints "<name> says: Woof!"
#         - jump() prints "<name> jumps <height*2> cm high!"
# Step 2: Create davids_dog and sarahs_dog objects.
# Step 3: Print each dog's info and call bark() and jump().
# Step 4: Compare the size of the two dogs.
# ============================================================

class Dog:
    def __init__(self, name, height):
        """
        Initialize a Dog object.
        Parameters:
            name (str): name of the dog
            height (int): height of the dog in cm
        """
        self.name = name
        self.height = height

    def bark(self):
        """Print a bark message."""
        print(f"{self.name} says: Woof!")

    def jump(self):
        """Print a jump message with height * 2."""
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 30)

# Step 3: Print info and call methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare the size of the two dogs
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")
