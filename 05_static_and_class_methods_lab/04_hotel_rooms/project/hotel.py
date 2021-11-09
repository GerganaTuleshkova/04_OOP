from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def find_room_by_number(self, room_number):
        found_rooms = [r for r in self.rooms if r.number == room_number]
        return found_rooms[0]

    def take_room(self, room_number, people):
        room = self.find_room_by_number(room_number)
        if room.take_room(people):
            return
        self.guests += room.guests

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        guest_to_deduct = room.guests

        if room.free_room():
            return
        self.guests -= guest_to_deduct

    def status(self):

        free_rooms_numbers = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
                           f"Free rooms: {', '.join(free_rooms_numbers)}\n" \
                           f"Taken rooms: {', '.join(taken_rooms)}"





