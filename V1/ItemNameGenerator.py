from random import randint

class ItemNameGenerator:
    def __init__(self, itemListFilePath : str = 'WeaponTypes.txt', adjListFilePath : str = 'Descriptions.txt'):
        adjFile    = open(adjListFilePath, "r")
        itemFile = open(itemListFilePath, "r")
        
        self.adjList    = [line.strip().title() for line in adjFile]
        self.itemList = [line.strip().title() for line in itemFile]
        
        adjFile.close()
        itemFile.close()

    def generateName(self) -> str:
        return self.adjList[randint(0, len(self.adjList) - 1)] + " " + self.itemList[randint(0, len(self.itemList) - 1)]
        

# TEST #

# weaponFile = open('WeaponTypes.txt', "r")

# gen = ItemNameGenerator() 
# for i in range(100):
#     print(gen.generateName())