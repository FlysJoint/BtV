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
global moves
moves = 0

class Room(object):
    tunnels = []

    def __init__(self, name, description, exits, pos):
        self.name = name
        self.description = description
        self.exits = exits
        self.pos = pos

    def describe(self):
        print("\033[H\033[J") 
        debug()
        # print(self.pos)
        print('You are in the %s. %s' % (self.name, self.description))
        prompt()


def prompt():
    print('There are exits: %s' % current_room.exits)
    my_action = input('What do you want to do? : ')
    action(my_action)


def action(my_action):
    global current_room
    global moves
    moves += 1
    debug()
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

def debug():
    global moves
    global current_room
    print('Moves: %s, Pos: %s, Room: %s\n' % (str(moves), str(current_room.pos), current_room.name))


def find_room(x, y):
    global current_room
    if x == 0 and y == 0:
        current_room = stacks
    elif x == 1 and y == 0:
        current_room = library
    elif x == 1 and y == 1:
        current_room = north_corridor
    elif x == 0 and y == 1:
        current_room = northwest_corridor
    elif x == 0 and y == 2:
        current_room = basement
    else:
        print('Trying to find x:%s, y:%s' % (x, y))
    print('moving to: ' + current_room.name)
    current_room.describe()


library = Room(
    'Library',
    'Bookcases and bookcases of ancient, arcane texts line the walls.',
    ['west', 'south'],
    [1, 0]
    )

stacks = Room(
    'Stacks',
    'Piles of musty tomes tower above you.',
    ['east'],
    [0, 0]
    )

north_corridor = Room(
    'North Corridor',
    'Students hustle and bustle on their way to class',
    ['north', 'west', 'east', 'south'],
    [1, 1]
)

northwest_corridor = Room(
    'Northwest Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south'],
    [0, 1]
)

basement= Room(
    'Basement',
    'Drips echo off rusty metal pipes. You can hear a rat scurrying. Amy?',
    ['north'],
    [0, 2]
)

find_room(1, 0)