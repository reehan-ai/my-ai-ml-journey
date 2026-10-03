import os

# Use the folder where this script is saved
directory = os.path.dirname(os.path.abspath(__file__))

# Print each item in the directory
for item in os.listdir(directory):
    print(item)