# Author: Christian Griessel
# nested loop program
# it displays two rows, each containing seven @ symbols

for i in range(2):
    for j in range(7):
        print('@', end='')
    print()

# Note to Ray: The problem doesn't say anything about modifying the print statement but idk if this
# is possible without adding end = ''
