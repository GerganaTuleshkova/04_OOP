from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

ornament = Ornament()
plant_orchid = Plant()
plant_orchid_2 = Plant()

repository = DecorationRepository()

repository.add(ornament)
repository.add(plant_orchid)
repository.add(plant_orchid_2)

print(repository.remove(plant_orchid_2))
print(repository.find_by_type("Plant"))

fish_a = FreshwaterFish("Ariel", "cold fish", 2.50)
print(fish_a.size)
print(fish_a.eat())
print(fish_a.size)

fish_s = SaltwaterFish("Kiki", "cold fish", 5.50)
print(fish_s.size)
print(fish_s.eat())
print(fish_s.size)



print(repository.find_by_type("Plant"))


fresha = FreshwaterAquarium("Freshy")
fresha.add_fish(fish_a)
fresha.add_decoration(ornament)
fresha.add_decoration(plant_orchid)

print(fish_a.size)

fresha.feed()
print(fish_a.size)

c = Controller()

print(c.add_aquarium("FreshwaterAquarium", "Fiorii-F"))
print(c.add_aquarium("SaltwaterAquarium", "Sisi-F"))
print(c.add_decoration("Plant"))
print(c.add_decoration("Ornament"))
print(c.add_decoration("Pya"))


print(c.insert_decoration("Sisi-F", "Plant"))
print(c.insert_decoration("Sisi-F", "Ornament"))



print(c.add_fish("Sisi-F", "SaltwaterFish", "ariel", "cold fish", 4.50))
print(c.add_fish("Sisi-F", "SaltwaterFish", "shaumi", "cold fish", 4.50))

print(c.report())





