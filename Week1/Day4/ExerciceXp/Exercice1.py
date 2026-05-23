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




