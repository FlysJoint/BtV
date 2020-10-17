#!/usr/bin/python3

# TODO:
# navigation (including not going off the map or through walls)
# secret tunnels (going through walls!)
# random attacks
# day/night cycle
# random spawns
# combat
# inventory

map = []
global current_room

class Room(object):
    tunnels = []

    def __init__(self, name, description, exits, pos):
        self.name = name
        self.description = description
        self.exits = exits
        self.pos = pos

    def describe(self):
        print("\033[H\033[J") 
        print(self.pos)
        print(self.description)
        # print('There are exits: %s' % self.exits)
        prompt()


def prompt():
    print('There are exits: %s' % current_room.exits)
    my_action = input('What do you want to do? : ')
    action(my_action)


def action(my_action):
    global current_room
    if my_action in current_room.exits:
        print('going %s from %s...' % (my_action, current_room.name))
        if my_action == 'west':
            find_room(current_room.pos[0] - 1, current_room.pos[1])
        elif my_action == 'east':
            find_room(current_room.pos[0] + 1, current_room.pos[1])
        elif my_action == 'north':
            find_room(current_room.pos[0], current_room.pos[1] - 1)
        elif my_action == 'south':
            find_room(current_room.pos[0], current_room.pos[1] + 1)
    elif my_action == 'quit':
        print('You run away, leaving the innocent people of Sunnydale to fend for themselves. They all die.')
    else:
        print('That is not a valid direction')
        prompt()


def find_room(x, y):
    global current_room
    if x == 0 and y == 0:
        current_room = stacks
    elif x == 1 and y == 0:
        current_room = library
    elif x == 1 and y == 1:
        current_room = north_corridor
    else:
        print('Trying to find x:%s, y:%s' % (x, y))
    print('moving to: ' + current_room.name)
    current_room.describe()


library = Room(
    'Library',
    'You are in the library. Bookcases and bookcases of ancient, arcane texts line the walls.',
    ['west', 'south'],
    [1, 0]
    )

stacks = Room(
    'Stacks',
    'You are in the stacks. Piles of musty tomes tower above you.',
    ['east'],
    [0, 0]
    )

north_corridor = Room(
    'North Corridor',
    'You are in the North Corridor. Students hustle and bustle on their way to class',
    ['north', 'west', 'east', 'south'],
    [1, 1]
)

find_room(1, 0)