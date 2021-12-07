from project.checker import Checker
from project.drink.water import Water
from project.drink.tea import Tea
from project.table.outside_table import OutsideTable
from project.table.inside_table import InsideTable
from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.table.table import Table


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = Checker.check_string(value)

    def add_food(self, food_type: str, name: str, price: float):
        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)

        if food is None:
            return

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        if drink_type == "Water":
            drink = Water(name, portion, brand)

        if drink is None:
            return

        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        if table is None:
            return

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    @staticmethod
    def check_item(item_name, menu):
        for item in menu:
            if item.name == item_name:
                return item
        return None

    def order_food(self, table_number: int, *args):
        table_with_order = self.find_table_by_number(table_number)
        if table_with_order is None:
            return f"Could not find table {table_number}"

        food_names_not_in_menu = []
        ordered_food = []

        for food_name in args:
            food_to_order = self.check_item(food_name, self.food_menu)
            if food_to_order is None:
                food_names_not_in_menu.append(food_name)
            else:
                ordered_food.append(food_to_order)
                table_with_order.food_orders.append(food_to_order)
        resulting_string = self.return_string_for_orders(table_with_order, food_names_not_in_menu, ordered_food)

        return resulting_string

    def return_string_for_orders(self, table_with_order: Table, item_names_not_in_menu, ordered_items):
        resulting_string = f"Table {table_with_order.table_number} ordered:"
        for item in ordered_items:
            #resulting_string += f"\n- {item.name}: {item.portion}g - {item.price}lv"
            resulting_string += f"\n{repr(item)}"

        resulting_string += f"\n{self.name} does not have in the menu:"
        for item_name in item_names_not_in_menu:
            resulting_string += f"\n{item_name}"

        return resulting_string

    # #check the 2 decimal places
    # def return_string_for_drinks(self, table_with_order: Table, item_names_not_in_menu, ordered_drinks):
    #     resulting_string = f"Table {table_with_order.table_number} ordered:"
    #     for item in ordered_drinks:
    #         resulting_string += f"\n - {item.name} {item.brand} - {item.portion}ml - {item.price}lv"
    #
    #     resulting_string += f"\n{self.name} does not have in the menu:"
    #     for item_name in item_names_not_in_menu:
    #         resulting_string += f"\n{item_name}"
    #
    #     return resulting_string

    def order_drink(self, table_number: int, *args):
        table_with_order = self.find_table_by_number(table_number)
        if table_with_order is None:
            return f"Could not find table {table_number}"

        drink_names_not_in_menu = []
        ordered_drinks = []

        for drink_name in args:
            drink_to_order = self.check_item(drink_name, self.drinks_menu)
            if drink_to_order is None:
                drink_names_not_in_menu.append(drink_name)
            else:
                table_with_order.drink_orders.append(drink_to_order)
                ordered_drinks.append(drink_to_order)
        resulting_string = self.return_string_for_orders(table_with_order, drink_names_not_in_menu, ordered_drinks)

        return resulting_string

    def leave_table(self, table_number: int):
        table_to_clean = self.find_table_by_number(table_number)
        bill = table_to_clean.get_bill()
        self.total_income += bill
        table_to_clean.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        resulting_string = ""
        for table in self.tables_repository:
            resulting_string += table.free_table_info()
            resulting_string += "\n"
        return resulting_string.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


