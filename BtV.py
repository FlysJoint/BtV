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
    night = ''

    def __init__(self, name, description, exits, pos, tunnels):
        self.name = name
        self.description = description
        self.exits = exits
        self.pos = pos
        self.tunnels = tunnels

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
    elif my_action in current_room.tunnels:
        find_room(current_room.tunnels[1], current_room.tunnels[2])
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
        current_room = alley
    elif x == 0 and y == 1:
        current_room = northwest_corridor
    elif x == 1 and y == 1:
        current_room = north_corridor
    elif x == 2 and y == 1:
        current_room = northeast_corridor
    elif x == 3 and y == 1:
        current_room = sports_field
    elif x == 4 and y == 1:
        current_room = bronze
    elif x == 0 and y == 2:
        current_room = basement
    elif x == 1 and y == 2:
        current_room = lockers
    elif x == 2 and y == 2:
        current_room = restroom
    elif x == 3 and y == 2:
        current_room = giles_house
    elif x == 4 and y == 2:
        current_room = street_7
    elif x == 0 and y == 3:
        current_room = principal_office
    elif x == 1 and y == 3:
        current_room = south_corridor
    elif x == 2 and y == 3:
        current_room = computer_room
    elif x == 3 and y == 3:
        current_room = magic_shop
    elif x == 4 and y == 3:
        current_room = street_6
    elif x == 0 and y == 4:
        current_room = buffy_house
    elif x == 1 and y == 4:
        current_room = street_2
    elif x == 2 and y == 4:
        current_room = street_3
    elif x == 3 and y == 4:
        current_room = street_4
    elif x == 4 and y == 4:
        current_room = street_5
    elif x == 0 and y == 5:
        current_room = willow_house
    elif x == 1 and y == 5:
        current_room = street_1
    elif x == 2 and y == 5:
        current_room = graveyard
    elif x == 3 and y == 5:
        current_room = tomb
    elif x == 4 and y == 5:
        current_room = angel_house
    else:
        print('Trying to find x:%s, y:%s' % (x, y))
    print('moving to: ' + current_room.name)
    current_room.describe()

stacks = Room(
    'Stacks',
    'Piles of musty tomes tower above you.',
    ['east'],
    [0, 0],
    []
    )

library = Room(
    'Library',
    'Bookcases and bookcases of ancient, arcane texts line the walls.',
    ['west', 'south'],
    [1, 0],
    []
    )

cafeteria = Room(
    'Cafeteria',
    'The stench of stale mashed potato hangs heavy in the air.',
    ['south'],
    [2, 0],
    []
    )

bleachers = Room(
    'Bleachers',
    'Sicknotes watch on as the athletes run laps',
    ['south'],
    [3, 0],
    []
    )

alley = Room(
    'Alley',
    'Litter flutters between rusty garbage cans. Somewhere a dog barks.',
    ['south'],
    [4, 0],
    ['east', 3, 5]
    )

northwest_corridor = Room(
    'Northwest Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south'],
    [0, 1],
    []
    )

north_corridor = Room(
    'North Corridor',
    'Students hustle and bustle on their way to class',
    ['north', 'west', 'east', 'south'],
    [1, 1],
    []
    )

northeast_corridor = Room(
    'Northeast Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south', 'north', 'west'],
    [2, 1],
    []
    )

sports_field = Room(
    'Sports Field',
    'Jocks run plays while cheerleaders dance their acrobatic routines',
    ['north', 'west', 'east'],
    [3, 1],
    []
    )

bronze = Room(
    'Bronze',
    'Indie bands rock out to the tune of pool balls being sunk and drinks being drunk',
    ['south', 'west', 'north'],
    [4, 1],
    []
    )

basement = Room(
    'Basement',
    'Drips echo off rusty metal pipes. You can hear a rat scurrying. Amy?',
    ['north'],
    [0, 2],
    ['west', 4, 5]
    )

lockers = Room(
    'Lockers',
    'Locker doors slam open and shut, a constant cacophony of clamour',
    ['south', 'north'],
    [1, 2],
    []
    )

restroom = Room(
    'Restroom',
    'A long mirror reflects the broken cubicles opposite. Some students giggle as you enter and run out.',
    ['north'],
    [2, 2],
    []
    )

giles_house = Room(
    'house of Giles',
    'The house is filled with armour, weapons and books from long ago. And an awful lot of tea.',
    ['east'],
    [3, 2],
    []
    )

street_7 = Room(
    'Street',
    'STREET DESCRIPTION',
    ['south', 'west', 'north'],
    [4, 2],
    []
    )

principal_office = Room(
    'Principal\'s Office',
    'The throne room of the most evil demon of them all.',
    ['east'],
    [0, 3],
    []
    )

south_corridor = Room(
    'South Corridor',
    'Students hustle and bustle on their way to class',
    ['east', 'south', 'north', 'west'],
    [1, 3],
    []
    )

computer_room = Room(
    'Computer Room',
    'Beeps and boops can be heard over the noise of blisteringly fast 14.4 modems',
    ['west'],
    [2, 3],
    []
    )

magic_shop = Room(
    'Magic Box',
    'Strange things in jars, strange smells from boxes, strange noises from books. Strange.',
    ['south'],
    [3, 3],
    []
    )

street_6 = Room(
    'Street',
    'STREET DESCRIPTION',
    ['south', 'north'],
    [4, 3],
    []
    )

buffy_house = Room(
    'house of Buffy',
    'Strange art adorns the walls inside and a thin layer of dust covers the garden.',
    ['south'],
    [0, 4],
    []
    )

street_2 = Room(
    'Street',
    'Students in various 90s fashions troop in and out of the high school entrance..',
    ['east', 'north', 'south'],
    [1, 4],
    []
    )

street_3 = Room(
    'Street',
    'Abandoned buildings and lonely car parks compound the desolation.',
    ['east', 'west'],
    [2, 4],
    []
    )

street_4 = Room(
    'Street',
    'Clothes shops, a costume shop and more clothes shops. Cordelia would be very happy.',
    ['east', 'west', 'north'],
    [3, 4],
    []
    )

street_5 = Room(
    'Street',
    'STREET DESCRIPTION',
    ['south', 'west', 'north'],
    [4, 4],
    []
    )

willow_house = Room(
    'house of Willow',
    'Downstairs it looks like a typical Jewish family home, but upstairs there is a heavy Wicca influence.',
    ['east', 'north'],
    [0, 5],
    []
    )

street_1 = Room(
    'Street',
    'Suburban houses gradually give way in style to more gothic buildings.',
    ['east', 'north', 'west'],
    [1, 5],
    []
    )

graveyard = Room(
    'Graveyard',
    'Unkempt tombstones protrude from the ground like negelected teeth.',
    ['east', 'west'],
    [2, 5],
    []
    )

tomb = Room(
    'Tomb',
    'Oil lamps illuminate a small chamber decorated by vases and morbid artefacts.',
    ['west'],
    [3, 5],
    ['south', 4, 1]
    )

angel_house = Room(
    'house of Angel',
    'There are no mirrors, a lot of art and large curtains and he really needs to sweep these leaves away.',
    ['north'],
    [4, 5],
    ['east', 0, 2]
    )

find_room(1, 0)