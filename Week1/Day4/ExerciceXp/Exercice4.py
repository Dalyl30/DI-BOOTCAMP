
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