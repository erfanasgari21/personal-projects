from random import random, seed
from math import floor

# Declerations:
# Declaring the table with 10 rows and 10 columns containong "" character:
islands = [["" for i in range(10)] for j in range(10)]

# Populating 11 random cells with R (Rabbit)
for i in range(0, 11):
    # Repeating the placing progress until finding an unoccupied cell
    while(True):
        # A random cell has a random index of row and column, each between 0 and 9
        m = floor(random()*10)
        n = floor(random()*10)
        if (islands[m][n] == ""):
            islands[m][n] = "R"
            # Finally an empty place is found and it's time to stop looking for one
            break

# Iterating the islands 2d array in order to print them
# Iterating the rows (islands[row])
for row in islands:
    # Iterating the columns (islands[row][item])
    for item in row:
        # Printing the cells considering their length in order to keep the width of each cell on 3
        print(item + (" " * (3-len(item))), end="")
    # After printing each row a vertical line is printed to show the end of the table
    print("|")
