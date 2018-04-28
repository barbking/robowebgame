# From Learn Python the Hard Way

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
'''
The Google AI robot army is taking over the world and destroying all humankind.
You are the only member left of the secret Duck Duck Go rebels with access to the
main server room that is controlling the Google AI army.  Your last mission is to 
get the neutron destruct bomb from the Weapons Armory, put it in the server room, 
and blow it up after getting into your escape hovercraft.
            
You're running down the central corridor to the Weapons Armory when a robot
jumps out.  It's blocking the door to the Armory and about to blast you with its
ray gun.
            
Options: shoot, dodge, ask Siri for help
''')

laser_weapon_armory = Room('Laser Weapon Armory',
'''
Lucky for you were able to ask Siri on your iPhone for help on how to dodge robots.
Siri distracts the robot by insulting Google's AI, while Siri and the Google AI
robot exchange insults, you shot the robot in its glass eyes and jump through
the Amory door.
''')

the_server_room = Room('The Server Room',
'''
You burst into the server room with the neutron destruct bomb under your arm
and surprise 5 Google AI robots guarding the room.  They haven't pulled their
weapons out yet, as they see the active omb under your arm and don't want to
set it off.
''')

escape_hovercraft = Room("Escape Hovercraft",
'''
You rush outside desperately trying to make it to the escape Duck Duck Go hovercrafts 
before the whole building explodes.  It seem like hardly any robots are in the area,
so your run is clear of interference.  You get to the parking lot and need to
pick one.  Some have been damaged by robots but you don't have time to check
them all.  There are five hovercraft, pick one to take.
''')

the_end_winner = Room('The End',
'''
You jump into the hovercraft 2 and hit the go button.  The hovercraft
easily takes off in the air.  As it flies into the sky, you see the server building
explode...taking out the Google Robot AI army control.  You won!
''')

the_end_loser = Room("The End",
'''
You jump into a random pod and hit go button.  The hovercraft takes off but
then implodes as the engine ruptures, blowing you up into a million pieces.
''')

the_end_loser_dodge = Room("The End",
'''
Lise a world class boxer you dodge, weave, slip and slide right as
the robot's blaster cranks a laser past your head.  In the middle of your
artful dodge your foot slips and you bang your head on the metal wall and
pass out.  You wake up shortly after only to die as the robot blasts you
with it's laser.
''')

escape_hovercraft.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_server_room.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_hovercraft
})

laser_weapon_armory.add_paths({
    '8132': the_server_room,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': the_end_loser_dodge,
    'ask Siri for help': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    '''
    There is a potential security problem here.
    Who gets to set name?  Cna that expose a variable?
    '''
    return globals().get(name)

def name_room(room):

    for key, value in globals().items():
        if value == room:
            return key