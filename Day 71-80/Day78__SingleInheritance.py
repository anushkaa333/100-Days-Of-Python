class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(f"{self.name} can make any sound, species {self.species}")

class dog(animal):
    def __init__(self, name, bread):
        self.bread = bread
        animal.__init__(self, name, species="log")

    def sound(self):
        print(f"{self.bread} Bark!")


d = dog("abc", "lab")
d.bread = "german"
d.dog_sound()
d.sound()
# german Bark!
# abc can make any sound, species log