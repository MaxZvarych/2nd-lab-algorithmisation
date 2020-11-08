class Hamster:
    def __init__(self,  hunger=1, greediness=1):
        self.hunger=hunger
        self.greediness=greediness


    def __str__(self):
        return "Hamster:" + \
               ", hunger:" + str(self.hunger) +\
               ", greediness:" + str(self.greediness)

    def calculate_total_food_consumption(self, amount):
        return self.hunger + self.greediness*(amount-1)
