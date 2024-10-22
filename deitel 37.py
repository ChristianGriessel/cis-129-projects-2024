# Author: Christian Griessel
# square and cube calculator
# it displays the squares and cubes of int 1-5 all within 1 loop with everything justified right on the print

print(f"number" + "square".rjust(10) + "cube".rjust(10))
for i in range(6):
    print(f"{i}".rjust(6) + f"{i ** 2}".rjust(10) + f"{i ** 3}".rjust(10))
