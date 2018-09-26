

class Message:
    def __init__(self):
        pass
    def update(self, gold):
        if gold <= 499:
            print ("Your shop is a barren wasteland.")
        elif gold >= 500 <= 999:
            print ("Locals are astonished to discover that there is a shop in their town.")
        elif gold >= 1000 <= 1999:
            print ("The town Crier has began to advertise your shop!")
        elif gold >= 2000 <= 4999:
            print ("Traders passing through town hear of your shop and begin to visit regularly.")
        elif gold >= 5000 <= 9999:
            print ("Adventurers on their travels begin to visit your shop to refill on their needs.")
        elif gold >= 10000 <= 24999:
            print ("You see your first hero shopping at your shop.")
        elif gold >= 25000 <= 49999:
            print ("Your shop has became a landmark on most maps.")
        elif gold >= 50000 <= 99999:
            print ("Knights, Adventurers and Heroes are very common customers.")
        elif gold >= 100000 <= 499999:
            print ("Your shop is listed as the best shop in the land by Ye Old Times!")
        elif gold >= 500000 <= 1000000:
            print ("Your shop has became so well known throughout the land that the king himself makes a visit.")
        elif gold == 1000000:
            print ("The King is so pleased with your shop that he decrees you as the Tomato Tycoon! You have successfully created the greatest shop in history! Congratulations on beating Tomato Tycoon!")
        else:
            print ("The King is so pleased with your shop that he decrees you as the Tomato Tycoon! You have successfully created the greatest shop in history! Congratulations on beating Tomato Tycoon!")