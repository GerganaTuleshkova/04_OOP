from project2.astronaut.astronaut import Astronaut
from project2.astronaut.astronaut_repository import AstronautRepository
from project2.astronaut.biologist import Biologist
from project2.astronaut.geodesist import Geodesist
from project2.astronaut.meteorologist import Meteorologist
from project2.planet.planet import Planet
from project2.space_station import SpaceStation

nasa_station = SpaceStation()

earth = Planet("Earth")
venera = Planet("Venera")

biologist_pesho = Biologist("Pesho")
biologist_gosho = Biologist("Goho")
biologist_ivan = Biologist("Ivan")

meteorologist_john = Meteorologist("John")
meteorologist_steve = Meteorologist("Steve")
meteorologist_kafka = Meteorologist("Kafka")

geodesist_anna = Geodesist("Anna")
geodesist_iva = Geodesist("Iva")
geodesist_elena = Geodesist("Elena")


nasa_station.add_astronaut("Biologist", "Pesho")
nasa_station.add_astronaut("Biologist", "Gosho")
# nasa_station.add_astronaut("Meteorologist", "Steve")
# nasa_station.add_astronaut("Meteorologist", "John")
# nasa_station.add_astronaut("Meteorologist", "Kafka")
# nasa_station.add_astronaut("Geodesist", "Elena")
# nasa_station.add_astronaut("Geodesist", "Anna")
# nasa_station.add_astronaut("Geodesist", "Iva")
# nasa_station.add_astronaut("Geodesist", "Iva")


nasa_station.add_planet("Mars", "sand, water, dust, p, i, o, l, k, t, r")
nasa_station.add_planet("Jupiter", "gold, water, k, l, m, g, r, s, a")
nasa_station.add_planet("Jupiter", "gold water")

for ast in nasa_station.astronaut_repository.astronauts:
    for _ in range(5):
        ast.breathe()

print(nasa_station.send_on_mission("Mars"))
print(nasa_station.report())


print(nasa_station.send_on_mission("Jupiter"))
print(nasa_station.report())








