class Vertex:

    def __init__(self, name, value=1, connections={}):
        self.name = name
        self.value = value
        self.connections = connections

    def __repr__(self):
        return "%s(%d)" % (self.name, self.value)


class FlowNetwork:

    def __init__(self):
        self.groups_to_add = set()
        self.full_rooms = set()

    def add_vertex(self, vertex):
        if vertex.name[0] == "g":
            self.groups_to_add.add(vertex)
        if vertex.name[0] == "s":
            self.full_rooms.add(vertex)
        return vertex


def min_but_more_than(room_set, group_size):
    suitable_room = max(room_set, key=lambda x: x.value)
    for room in room_set:
        if room.value >= group_size and room.value < suitable_room.value:
            suitable_room = room
    return suitable_room

g = FlowNetwork()

groups_count = int(input("How many groups? "))
classrooms_count = int(input("How many classrooms? "))

groups_sizes = [int(input("g%d: " % i)) for i in range(1, groups_count + 1)]
classrooms_sizes = [int(input("c%d: " % i)) for i in range(1, classrooms_count + 1)]

groups_names = ["g%d" % (x+1) for x in range(groups_count)]
classrooms_names = ["s%d" % (x+1) for x in range(classrooms_count)]
time_slots = int(input("How many time slots? "))

groups = [g.add_vertex(Vertex(groups_names[i], groups_sizes[i])) for i in range(len(groups_names))]
classrooms = [g.add_vertex(Vertex(classrooms_names[i], classrooms_sizes[i])) for i in range(len(classrooms_sizes))]

for t in range(1, time_slots + 1):
    pair_exists = True
    while pair_exists:
        if g.full_rooms and g.groups_to_add:
            group_to_add = g.groups_to_add.pop()
            max_room = max(g.full_rooms, key=lambda x: x.value)
            if max_room.value >= group_to_add.value:
                min_room = min_but_more_than(g.full_rooms, group_to_add.value)
                g.full_rooms.remove(min_room)
                print("Time: %d, group %s,%3d in room %s,%3d" %
                      (t, group_to_add.name, group_to_add.value, min_room.name, min_room.value))
            else:
                g.groups_to_add.add(group_to_add)

        if g.full_rooms and g.groups_to_add:
            max_room = max(g.full_rooms, key=lambda x: x.value)
            min_group = min(g.groups_to_add, key=lambda x: x.value)
            if max_room.value < min_group.value:
                pair_exists = False
        else:
            pair_exists = False
    [g.add_vertex(Vertex(classrooms_names[i], classrooms_sizes[i])) for i in range(len(classrooms_sizes))]
