# ============================================================
# Exercise 1: Cats
# Instructions:
# Use the Cat class to create three cat objects.
# Create a function to find the oldest cat and display its details.
#
# Step 1: Create three cat objects with different names and ages.
# Step 2: Create a function that takes three cat objects,
#         compares their ages and returns the oldest one.
# Step 3: Print the oldest cat's details in the format:
#         "The oldest cat is <name>, and is <age> years old."
# ============================================================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Milo", 5)

# Step 2: Find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    """
    Find and return the oldest cat among three cat objects.
    Parameters: cat1, cat2, cat3 (Cat): cat objects with name and age
    Returns: Cat: the oldest cat object
    """
    return max([cat1, cat2, cat3], key=lambda cat: cat.age)

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


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


# ============================================================
# Exercise 3: Who is the song producer?
# Instructions:
# Create a Song class with a method to print lyrics line by line.
#
# Step 1: Create a Song class.
#         - __init__ takes lyrics (a list) as parameter.
#         - sing_me_a_song() prints each lyric on a new line.
# ============================================================

class Song:
    def __init__(self, lyrics):
        """
        Initialize a Song object.
        Parameters: lyrics (list): list of song lyric lines
        """
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Print each lyric line by line."""
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a lady who's sure",
                 "all that glitters is gold",
                 "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()


# ============================================================
# Exercise 4: Zoo
# Instructions:
# Create a Zoo class to manage animals.
# The class must allow adding, displaying, selling,
# and sorting animals alphabetically.
#
# Step 1: Create a Zoo class with:
#   - __init__(zoo_name): initializes name and empty animals list
#   - add_animal(new_animal): adds animal if not already in list
#   - get_animals(): prints all animals in the zoo
#   - sell_animal(animal_sold): removes animal if it exists
#   - sort_animals(): sorts and groups animals by first letter
#   - get_groups(): prints the grouped animals
# Step 2: Create a Zoo instance.
# Step 3: Call the Zoo methods to test adding, selling,
#         displaying, sorting and grouping animals.
# Bonus: Use *args to add multiple animals at once.
# ============================================================

class Zoo:
    def __init__(self, zoo_name):
        """
        Initialize a Zoo object.
        Parameters: zoo_name (str): name of the zoo
        """
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        """
        Add one or more animals to the zoo if not already present.
        Parameters: *new_animals (str): one or more animal names
        """
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        """Print all animals currently in the zoo."""
        print(f"Animals in {self.zoo_name}: {self.animals}")

    def sell_animal(self, animal_sold):
        """
        Remove an animal from the zoo if it exists.
        Parameters: animal_sold (str): name of the animal to remove
        """
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        """
        Sort animals alphabetically and group them by first letter.
        Returns: dict: dictionary with letters as keys and animal lists as values
        """
        sorted_list = sorted(self.animals)
        groups = {}
        for animal in sorted_list:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups

    def get_groups(self):
        """Print animals grouped by their first letter."""
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()