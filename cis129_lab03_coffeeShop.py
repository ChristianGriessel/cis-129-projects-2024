# Christian Griessel
# Coffee and Muffin program for CIS 129
# Calculates the price of various items and accounts for sales tax


def main():
    coffee_muffin_values = coffee_muffin_counter()
    printer(coffee_muffin_values[0], coffee_muffin_values[1])


def coffee_muffin_counter():
    """This function grabs the number of coffees and muffins while making sure that the numbers are ints and are realistic"""
    while True:
        # Prompt for muffins, sets value to None so if a string is typed it won't reset the loop back to muffins once muffins has a value
        number_of_muffins = None
        while number_of_muffins is None:
            try:
                number_of_muffins = int(input("HOW MANY MUFFINS IN THIS PURCHASE?: ")) # Forces int and forces a realistic number
                if number_of_muffins < 0 or number_of_muffins > 50:
                    print("UNREALISTIC MUFFIN COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                    number_of_muffins = None  # Reset for valid input before the loop starts again
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        # Prompt for coffees only once we have a confirmed int locked in for muffins
        while True:
            try:
                number_of_coffees = int(input("HOW MANY COFFEES IN THIS PURCHASE?: ")) # Forces int and forces a realistic number
                if number_of_coffees < 0 or number_of_coffees > 50:
                    print("UNREALISTIC COFFEE COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                else:
                    break # Assuming a value for muffin and a value for coffee loop is broken and values are returned
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        # Return two valid values
        return number_of_muffins, number_of_coffees





def printer(coffee, muffins):
    """Prints out a mock recipt. All math handled in the fstring"""
    print("***************************************\n"
          "My Coffee and Muffin Shop\n"
          "Number of coffees bought?\n"
          f"{coffee}\n"
          "Number of muffins bought?\n"
          f"{muffins}\n"
          "***************************************\n\n"
          "***************************************\n"
          "My Coffee and Muffin Shop Receipt\n"
          # Multiplies price by number purchased and forces two decimal points. 
          f"{coffee} Coffee at $5 each: $ {float(coffee) * 5:.2f}\n"
          f"{muffins} Muffins at $4 each: $ {float(muffins) * 4:.2f}\n"
          # Multiplies totals by .06 to calculate tax. Forces two decimal points.
          f"6% tax: $ {(float(coffee) * 5 + float(muffins) * 4) * 0.06:.2f}\n"
          f"---------\n"
          # Multiplies totals by 1.06 to calculate total + tax. Forces two decimal points.
          f"Total: $ {(float(coffee) * 5 + float(muffins) * 4) * 1.06:.2f}\n"
          "***************************************")



if __name__ == '__main__':
    main()
