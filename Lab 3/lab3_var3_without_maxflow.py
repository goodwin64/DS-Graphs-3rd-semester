# author = "Max Donchenko (https://github.com/goodwin64)"

from random import randint


def add_vertex(name, value, some_dict):
    if name[0] == "g":
        some_dict[name] = value
    elif name[0] == "r":
        some_dict[name] = value


def min_but_more_than(rooms_dict, group_size):
    suitable_room_name = max(rooms_dict, key=lambda x: rooms_dict[x])
    for room_name in list(rooms_dict.keys()):
        if rooms_dict[suitable_room_name] > rooms_dict[room_name] >= group_size:
            suitable_room_name = room_name
    return suitable_room_name


def main():
    input_type = int(input("1 - Auto, 2 - Manual: "))
    if input_type == 1:
        groups = list(set([randint(1, 25) for i in range(randint(0, 9))]))
        rooms = list(set([randint(5, 100) for i in range(randint(0, 9))]))
        print(groups)
        print(rooms)
    elif input_type == 2:
        groups = list(map(int, input("Groups sizes list (separate them by comma): ").replace(" ", "").split(",")))
        rooms = list(map(int, input("Rooms sizes list (separate them by comma): ").replace(" ", "").split(",")))
        print(groups)
        print(rooms)
    else:
        print("Enter 1 or 2")
        main()

    groups_count = len(groups)
    rooms_count = len(rooms)

    groups_names = ["group %d" % (i+1) for i in range(groups_count)]
    rooms_names = ["room %d" % (i+1) for i in range(rooms_count)]

    time_slots = int(input("How many time slots? "))

    groups_to_add = {}
    full_rooms = {}

    [add_vertex(groups_names[i], groups[i], groups_to_add) for i in range(groups_count)]
    del groups, groups_count
    [add_vertex(rooms_names[i], rooms[i], full_rooms) for i in range(rooms_count)]

    for t in range(1, time_slots + 1):
        pair_exists = True
        while pair_exists:
            if full_rooms and groups_to_add:
                group_to_add_name = groups_names[0]
                group_to_add_size = groups_to_add.pop(groups_names[0])
                del groups_names[0]
                max_room_name = max(full_rooms, key=lambda x: full_rooms[x])
                max_room_size = full_rooms[max_room_name]
                if max_room_size >= group_to_add_size:
                    min_room_name = min_but_more_than(full_rooms, group_to_add_size)
                    print("Time: %d, %s,%3d in %s,%3d" %
                          (t, group_to_add_name, group_to_add_size, min_room_name, full_rooms[min_room_name]))
                    del full_rooms[min_room_name]
                else:
                    groups_to_add[group_to_add_name] = group_to_add_size
            if full_rooms and groups_to_add:
                max_room_size = max(full_rooms.values(), key=lambda x: x)
                min_group_size = min(groups_to_add.values(), key=lambda x: x)
                if max_room_size < min_group_size:
                    pair_exists = False
            else:
                pair_exists = False
        [add_vertex(rooms_names[i], rooms[i], full_rooms) for i in range(rooms_count)]

main()
