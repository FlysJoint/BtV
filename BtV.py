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
        print(self.pos)
        print(self.description)
        print('There are exits: %s' % self.exits)
        prompt()
        

def prompt():
    my_action = input('What do you want to do? : ')
    action(my_action)

def action(my_action):
    global current_room
    print(current_room.name)
    print(current_room.pos)
    print(current_room.exits)
    if my_action in current_room.exits:
        print('going %s...' % my_action)
        if my_action == 'west':
            find_room(current_room.pos[0] - 1, current_room.pos[1])
        if my_action == 'east':
            find_room(current_room.pos[0] + 1, current_room.pos[1])
    else:
        print('That is not a valid direction')

def find_room(x, y):
    global current_room
    if x == 0 and y == 0:
        current_room = stacks
        # print('moving to stacks')
    elif x == 1 and y == 0:
        current_room = library
        # print('moving to library')
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

find_room(1, 0)