# Author: Christian Griessel
# Bottle Counter
# Returns the amount paid out depending on how many bottles recieved


NBR_OF_DAYS = 7
PAYOUT_PER_BOTTLE = .10


def main():
    totalBottles = 0
    counter = 1
    while counter <= NBR_OF_DAYS:
        todayBottles = int(input(f"How many bottles received on day number {counter}?: "))
        totalBottles += todayBottles
        counter += 1
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    print(f"The total numbers of bottles collected is {totalBottles}")
    print(f"The total paid out is ${totalPayout:.2f}")
    keep_going = (input("Keep going? (y/n): ")).lower()
    if keep_going == "y":
        main()
    else:
        print('Thank you, terminating now')


main()
