class Factory:

    def __init__(self, n, c, tt):
        self.name = n
        self.colour = c 
        self.toytype = tt

    def material(self):
        print("Buying materials")

    def sew(self):
        print("Sewing a toy")

    def dye(self):
        print("Dying a toy") 

class Toys(Factory):
    def newtoy(self):
        return f"{n}, {c}, {tt}"


new_toy = Toys("Babyborn", "colorful", "Dolls")

new_toy.material()
new_toy.sew()
new_toy.dye()
print(new_toy.newtoy)
