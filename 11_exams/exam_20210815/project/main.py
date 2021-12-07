from baked_food.bread import Bread
from baked_food.cake import Cake
from drink.tea import Tea
from drink.water import Water
from project.bakery import Bakery
from table.inside_table import InsideTable
from table.outside_table import OutsideTable

bread = Bread("white bread", 2.5666)
cake = Cake("garaz", 60)

water = Water("Natural water", 500, "Devin")

tea = Tea("Lemon", 300, "Lipton")


inside_table = InsideTable(3, 5)
inside_table.order_drink(water)
inside_table.order_food(bread)
inside_table.order_food(cake)
inside_table.reserve(4)
inside_table.clear()

outside_table = OutsideTable(66, 6)


bakery = Bakery("Fancy bakery")
print(bakery.add_food("Bread", "black bread", 2.00))
print(bakery.add_food("Bread", "white bread", 2.00))

print(bakery.add_drink("Tea", "Lemon", 250, "Lipton"))
print(bakery.add_drink("Water", "Mineral", 250, "Devin"))

outside_table2= (bakery.add_table("OutsideTable", 55, 7))
print(bakery.add_table("InsideTable", 30, 7))

print(bakery.reserve_table(6))
print(bakery.reserve_table(9))

print(bakery.order_food(55, "black bread", "chicken", "chicken", "white bread", "white bread"))

print(bakery.order_food(5565, "black bread", "chicken", "chicken", "white bread", "white bread"))


print(bakery.order_drink(55, "Lemon", "coke", "chicken", "Mineral", "Mineral"))

# print(bakery.leave_table(55))
# print(bakery.get_free_tables_info())
# print(bakery.get_total_income())





