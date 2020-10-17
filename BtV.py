#!/usr/bin/python3

# TODO:
# secret tunnels (going through walls!)
# random attacks
# day/night cycle - needs to be every 6 moves instead of every other
# random spawns
# combat
# inventory

map = []
global current_room
global moves
moves = 0

class Room(object):
    tunnels = []
    night = ''

    def __init__(self, name, description, exits, pos):
        self.name = name
        self.description = description
        self.exits = exits
        self.pos = pos

    def describe(self):
        global moves
        print("\033[H\033[J") 
        debug()
        if moves % 2 == 0:
            self.night = ''
        else:
            self.night = ' at night'
        print('You are in the %s%s. %s' % (self.name, self.night, self.description))
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
    elif x == 2 and y == 0:
        current_room = cafeteria
    elif x == 3 and y == 0:
        current_room = bleachers
    elif x == 4 and y == 0:
        current_room = bronze
    elif x == 0 and y == 1:
        current_room = northwest_corridor
    elif x == 1 and y == 1:
        current_room = north_corridor
    elif x == 2 and y == 1:
        current_room = northeast_corridor
    elif x == 3 and y == 1:
        current_room = sports_field
    elif x == 0 and y == 2:
        current_room = basement
    elif x == 1 and y == 2:
        current_room = lockers
    elif x == 2 and y == 2:
        current_room = restroom
    elif x == 0 and y == 3:
        current_room = principal_office
    elif x == 1 and y == 3:
        current_room = south_corridor
    elif x == 2 and y == 3:
        current_room = computer_room
    else:
        print('Trying to find x:%s, y:%s' % (x, y))
    print('moving to: ' + current_room.name)
    current_room.describe()

stacks = Room(
    'Stacks',
    'Piles of musty tomes tower above you.',
    ['east'],
    [0, 0]
    )

library = Room(
    'Library',
    'Bookcases and bookcases of ancient, arcane texts line the walls.',
    ['west', 'south'],
    [1, 0]
    )

cafeteria = Room(
    'Cafeteria',
    'The stench of stale mashed potato hangs heavy in the air.',
    ['south'],
    [2, 0]
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

northeast_corridor = Room(
    'Northeast Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south', 'north', 'west'],
    [2, 1]
)

basement = Room(
    'Basement',
    'Drips echo off rusty metal pipes. You can hear a rat scurrying. Amy?',
    ['north'],
    [0, 2]
)

restroom = Room(
    'Restroom',
    'A long mirror reflects the broken cubicles opposite. Some students giggle as you enter and run out.',
    ['north'],
    [2, 2]
)

sports_field = Room(
    'Sports Field',
    'Jocks run plays while cheerleaders dance their acrobatic routines',
    ['north', 'west', 'east'],
    [3, 1]
)

bleachers = Room(
    'Bleachers',
    'Sicknotes watch on as the athletes run laps',
    ['south'],
    [3, 0]
)

bronze = Room(
    'Bronze',
    'Indie bands rock out to the tune of pool balls being sunk and drinks being drunk',
    ['south'],
    [4, 0]
)

lockers = Room(
    'Lockers',
    'Locker doors slam open and shut, a constant cacophony of clamour',
    ['south', 'north'],
    [1, 2]
)

south_corridor = Room(
    'South Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south', 'north', 'west'],
    [1, 3]
)

principal_office = Room(
    'Principal\'s Office',
    'The throne room of the most evil demon of them all.',
    ['east'],
    [0, 3]
)

computer_room = Room(
    'Computer Room',
    'Beeps and boops can be heard over the noise of blistering 14.4 modems',
    ['west'],
    [2, 3]
)

find_room(1, 0)